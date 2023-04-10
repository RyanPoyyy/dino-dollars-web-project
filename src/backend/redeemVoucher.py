from flask import Flask, request, jsonify
from flask_cors import CORS

import os, sys

import requests
from invokes import invoke_http

# import amqp_setup
# import pika
import json

app = Flask(__name__)
CORS(app)

@app.route("/redeem_voucher/<int:VID>", methods=['GET'])
def redeem_voucher(VID):
    status = updateVoucher(VID)
    return status
    
def updateVoucher(VID):
    url = "http://purchasedvoucher:5002/purchasedvoucher/" + str(VID)
    updateVoucher = invoke_http(url, method='PUT')
    return updateVoucher

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5010, debug=True)