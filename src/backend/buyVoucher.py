from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys
from os import environ

import requests
from invokes import invoke_http

import amqp_setup
import pika
import json

app = Flask(__name__)
CORS(app)

user_url = "http://user:5003/user/"
purchasedvoucher_url = "http://purchasedvoucher:5002/purchasedvoucher"   

@app.route("/buy_voucher/<int:UID>/<int:DDRequired>", methods=['POST'])
def buy_voucher(UID, DDRequired):
    if request.is_json:
        try:
            details = request.get_json()
            print("\nReceived an order in JSON:", details)

            # do the actual work
            # 1. Send order info {cart items}
            newVoucher = createNewVoucher(details)
            print(newVoucher)

            if newVoucher["code"] in range(200,300):
                user = getCurrentBalance(UID)

                if user["code"] in range(200,300):
                    currentBalance = user["data"]["Points"]
                    newBalance = currentBalance - DDRequired
                    print(f'currentBalance {currentBalance}')
                    print(f'newBalance {newBalance}')
                    print(f'DDRequired {DDRequired}')
                    print(type(newBalance))
                    newPoints = {"Points": newBalance}
                    result = updateUserBalance(newPoints, UID, newVoucher)
                    print('\n------------------------')
                    print('\nresult: ', result) 
                    return jsonify(result), result["code"]
                else:
                    return jsonify(user), user["code"]
                
                
            else:
                return jsonify(newVoucher), newVoucher["code"]
            

            # newVoucher = createNewVoucher()
            # newBalance = getCurrentBalance(UID) - Cost
            # updateNewBalance = updateUserBalance(UID) 
            # # purchasedVoucher = returnPurchasedVoucher(UID)
            # return newVoucher            

        except Exception as e:
            # Unexpected error in code
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            ex_str = str(e) + " at " + str(exc_type) + ": " + fname + ": line " + str(exc_tb.tb_lineno)
            print(ex_str)

            return jsonify({
                "code": 500,
                "message": "buyVoucher.py internal error: " + ex_str
            }), 500

    # if reached here, not a JSON request.
    return jsonify({
        "code": 400,
        "message": "Invalid JSON input: " + str(request.get_data())
    }), 400

def createNewVoucher(details):
    url = "http://purchasedvoucher:5002/purchasedvoucher" 
    newVoucher = invoke_http(url, method='POST', json=details)
    return newVoucher

def getCurrentBalance(UID):
    url = "http://user:5003/user/" + str(UID)
    user = invoke_http(url, method='GET')
    return user


def updateUserBalance(order, UID, newVoucher):
    # 2. Send the order info {cart items}
    # Invoke the order microservice
    print('\n-----Invoking order microservice-----')
    print(order)
    user_url = "http://user:5003/point/" + str(UID)
    print(user_url)
    order_result = invoke_http(user_url, method='PUT', json=order)
    print('order_result:', order_result)

    # Check the order result; if a failure, send it to the error microservice.
    code = order_result["code"]
    message = json.dumps(order_result)

    if code not in range(200, 300):
        # Inform the error microservice
        #print('\n\n-----Invoking error microservice as order fails-----')
        print('\n\n-----Publishing the (order error) message with routing_key=order.error-----')

        # invoke_http(error_URL, method="POST", json=order_result)
        amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.error", 
            body=message, properties=pika.BasicProperties(delivery_mode = 2)) 
        # make message persistent within the matching queues until it is received by some receiver 
        # (the matching queues have to exist and be durable and bound to the exchange)

        # - reply from the invocation is not used;
        # continue even if this invocation fails        
        print("\nOrder status ({:d}) published to the RabbitMQ Exchange:".format(
            code), order_result)

        # 7. Return error
        return {
            "code": 500,
            "data": {"order_result": order_result},
            "message": "Failure to update dino dollars balance sent for error handling."
        }

    # Notice that we are publishing to "Activity Log" only when there is no error in order creation.
    # In http version, we first invoked "Activity Log" and then checked for error.
    # Since the "Activity Log" binds to the queue using '#' => any routing_key would be matched 
    # and a message sent to “Error” queue can be received by “Activity Log” too.

    # else:
    #     # 4. Record new order
    #     # record the activity log anyway
    #     #print('\n\n-----Invoking activity_log microservice-----')
    #     print('\n\n-----Publishing the (order info) message with routing_key=order.info-----')        

    #     # invoke_http(activity_log_URL, method="POST", json=order_result)            
    #     amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="order.info", 
    #         body=message)

    formatted_body = {
        "type": "buy",
        "voucher" : newVoucher,
        "order_result": order_result
    }

    message = json.dumps(formatted_body)
    amqp_setup.channel.basic_publish(exchange=amqp_setup.exchangename, routing_key="buy.notifications", body=message, properties=pika.BasicProperties(delivery_mode = 2))
    
    print("\nOrder published to RabbitMQ Exchange.\n")
    return {
            "code": 200,
            "currentPoints": order_result["data"]["Points"],
            }    # - reply from the invocation is not used;
    # continue even if this invocation fails
    

# oversimplified one
# def updateUserBalance(UID):
#     url = "http://localhost:5003/point/" + str(UID)
#     updatedBalance = invoke_http(url, method='PUT')
#     return updatedBalance

# def returnPurchasedVoucher(UID):
#     url = "http://localhost:5002/purchasedvoucher/" + str(UID) 
#     purchasedVoucher = invoke_http(url, method='GET')
#     return purchasedVoucher


if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=6002, debug=True)
    # Notes for the parameters: 
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program, and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.
