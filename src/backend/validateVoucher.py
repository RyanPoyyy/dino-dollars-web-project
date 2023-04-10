from flask import Flask, request, jsonify
from flask_cors import CORS
import os, sys
from os import environ
import requests
from invokes import invoke_http
import json

app = Flask(__name__)
CORS(app)

user_url = environ.get('user_URL') or "http://localhost:5003/user/"
voucher_url = environ.get('voucher_URL') or "http://localhost:5001/voucher"

@app.route("/validate_voucher/<int:UID>", methods=['GET'])
def validate_voucher(UID):
    # Making sure that vouchers displayed to user are those that they have sufficient points for
    vouchers = getVouchers()
    points = getUserPoints(UID)
    
    voucherList = getAvailableVouchers(points, vouchers)
    available_voucher_list=voucherList[0]
    unavailable_voucher_list=voucherList[1]
    print(available_voucher_list)
    print(unavailable_voucher_list)
    return voucherList

def getUserPoints(UID):
    url = "http://user:5003/user/" + str(UID)
    getUser = invoke_http(url, method='GET')
    return str(getUser["data"]["Points"])
    
def getVouchers():
    url = "http://availablevoucher:5001/availablevoucher"
    getVouchers = invoke_http(url, method='GET')
    return getVouchers["data"]["AllVouchers"]

def getAvailableVouchers(points, vouchers):
    available_vouchers = []
    unavailable_vouchers = []
    total = []

    for voucher in vouchers:
        # return voucher

        if int(voucher['DDRequired']) <= int(points):

            available_vouchers.append(voucher)
        else:
            unavailable_vouchers.append(voucher)

    total.append(available_vouchers)
    total.append(unavailable_vouchers)
    return total

if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) + " for placing an order...")
    app.run(host="0.0.0.0", port=6001, debug=True)