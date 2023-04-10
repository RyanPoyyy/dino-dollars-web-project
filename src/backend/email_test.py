from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
import json
import os
import amqp_setup

monitorBindingKey="*.notifications"

def checkNotifType():
    amqp_setup.check_setup()

    queue_name = "Notifications"

    # set up a consumer and start to wait for coming messages
    amqp_setup.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    amqp_setup.channel.start_consuming() # an implicit loop waiting to receive messages; 
    #it doesn't exit by default. Use Ctrl+C in the command window to terminate it.    

def callback(channel, method, properties, body): # required signature for the callback; no return
    print("\nReceived an order log by " + __file__)

    message = json.loads(body)
    
    if message["type"] == "buy":
        sendBuyEmail(message)
    elif message["type"] == "accumulate":
        sendAccumulateEmail(message)
    print() # print a new line feed

def sendBuyEmail(payload):
    print("Recording an order log:")
    # {'code': 200, 'data': {'Email': 'ryanpoy.2021@scis.smu.edu.sg', 'LinkedAccs': [], 'Name': 'Poy', 'Password': 'password', 'Points': 2097, 'UID': 2}}
    
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    user = payload['order_result']['data']
    userEmail = user['Email']
    userName = user['Name']

    # APIKEY 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
    # response = requests.get("https://api.sendinblue.com/v3/")
    
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['api-key'] = 'Bearer'
    # Configure API key authorization: partner-key
    # configuration = sib_api_v3_sdk.Configuration()
    # configuration.api_key['partner-key'] = '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'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['partner-key'] = 'Bearer'

    # create an instance of the API class
    # api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "You earned some points!"
    html_content = "<html><body><h1>YAYYYY</h1> <br/> <p>You bought a voucher <br/> </p></body></html>"
    sender = {"name":"DinoDollars","email":"dinodollars@donotreply.com"}
    to = [{"email": userEmail ,"name": userName}]
    # headers = {"Some-Custom-Name":"unique-id-1234"}
    # params = {"parameter":"My param value","subject":"New Subject"}
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
    try:
        # Get your account information, plan and credits details
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)

def sendAccumulateEmail(payload):
    print("Recording an order log:")
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = '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'
    # {'code': 200, 'data': {'Email': 'ryanpoy.2021@scis.smu.edu.sg', 'LinkedAccs': [], 'Name': 'Poy', 'Password': 'password', 'Points': 2097, 'UID': 2}}
    
    user = payload['order_result']['data']
    userEmail = user['Email']
    userName = user['Name']
    userPoints = user['Points']

    # APIKEY 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
    # response = requests.get("https://api.sendinblue.com/v3/")
    
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['api-key'] = 'Bearer'
    # Configure API key authorization: partner-key
    # configuration = sib_api_v3_sdk.Configuration()
    # configuration.api_key['partner-key'] = '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'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['partner-key'] = 'Bearer'

    # create an instance of the API class
    # api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))
    
    api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
    subject = "You earned some points!"
    html_content = "<html><body><h1>Congrats</h1> <br/> <p>Your current points total is now: <br/> <h2>" + str(userPoints) + "</h2></p></body></html>"
    sender = {"name":"DinoDollars","email":"dinodollars@donotreply.com"}
    to = [{"email": userEmail ,"name": userName}]
    # headers = {"Some-Custom-Name":"unique-id-1234"}
    # params = {"parameter":"My param value","subject":"New Subject"}

    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, html_content=html_content, sender=sender, subject=subject)
    try:
        # Get your account information, plan and credits details
        api_response = api_instance.send_transac_email(send_smtp_email)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)

if __name__ == "__main__":  # execute this program only if it is run as a script (not by 'import')
    print("\nThis is " + os.path.basename(__file__), end='')
    print(": monitoring routing key '{}' in exchange '{}' ...".format(monitorBindingKey, amqp_setup.exchangename))
    checkNotifType()
