import imp

#!flask/bin/python
from datetime import timedelta
from flask import Flask, jsonify, request, make_response, current_app
from functools import update_wrapper

app = Flask(__name__)

@app.after_request # blueprint can also be app~~
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header["Access-Control-Allow-Credentials"]= True
    header["Access-Control-Allow-Methods"]='*'
    header["Access-Control-Allow-Headers"]='*'

    return response


# Accept JS / Accept UI

@app.route('/api/AcceptSuite/AcceptJS', methods=['GET'])
def get_AcceptJS():

    # to get parameters from the requested url
    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    token = request.args.get('token')

    print('Start create_an_accept_payment_transaction')

    # call API method
    modl = imp.load_source('modulename', 'AcceptSuite/create-an-accept-payment-transaction.py')
    result= modl.create_an_accept_payment_transaction(apiLoginId,apiTransactionKey,token)
    data = {
        "status": False,
        "successValue": None,
        "errorMessage": None
    }
    if result is not None:
      if result.messages.resultCode == "Ok":
        data={
            "status":True,
            "successValue":str(result.transactionResponse.transId),
            "errorMessage":None
           }
      else:
        data = {
              "status": False,
              "successValue": None,
              "errorMessage": str(result.messages.message[0]['text'].text)
        }

    print('End create_an_accept_payment_transaction')
    return jsonify(data)


# Accept Hosted

@app.route('/api/AcceptSuite/AcceptHosted', methods=['GET'])
def get_AcceptHosted():

    # to get parameters from the requested url
    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    iFrameCommunicatorUrl=request.args.get('iFrameCommunicatorUrl')
    customerId = request.args.get('customerId')
    print('Start get_an_accept_payment_page')

    # call API method
    modl = imp.load_source('modulename', 'AcceptSuite/get-an-accept-payment-page.py')
    result= modl.get_an_accept_payment_page(apiLoginId,apiTransactionKey,iFrameCommunicatorUrl,customerId)
    data = {
        "status": False,
        "successValue": None,
        "errorMessage": None
    }
    if result is not None:
      if result.messages.resultCode == "Ok":
        data={
            "status":True,
            "successValue":str(result.token),
            "errorMessage":None
           }
      else:
        data = {
              "status": False,
              "successValue": None,
              "errorMessage": str(result.messages.message[0]['text'].text)
        }
    print('End get_an_accept_payment_page')
    return jsonify(data)


# Accept Customer

@app.route('/api/AcceptSuite/AcceptCustomer', methods=['GET'])
def get_AcceptCustomer():

    # to get parameters from the requested url
    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    iFrameCommunicatorUrl=request.args.get('iFrameCommunicatorUrl')
    customerId = request.args.get('customerId')
    print('Start get_accept_customer_profile_page')

    # call API method
    modl = imp.load_source('modulename', 'AcceptSuite/get-accept-customer-profile-page.py')
    result= modl.get_accept_customer_profile_page(apiLoginId,apiTransactionKey,iFrameCommunicatorUrl,customerId)
    data = {
        "status": False,
        "successValue": None,
        "errorMessage": None
    }
    if result is not None:
      if result.messages.resultCode == "Ok":
        data={
            "status":True,
            "successValue":str(result.token),
            "errorMessage":None
           }
      else:
        data = {
              "status": False,
              "successValue": None,
              "errorMessage": str(result.messages.message[0]['text'].text)
        }
    print('End get_an_accept_payment_page')
    return jsonify(data)


# Validate Customer

@app.route('/api/AcceptSuite/ValidateCustomer', methods=['GET'])
def get_ValidateCustomer():

    # to get parameters from the requested url
    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    customerId = request.args.get('customerId')
    print('Start get_customer_profile')

    # call API method
    modl = imp.load_source('modulename', 'CustomerProfiles/get-customer-profile.py')
    result= modl.get_customer_profile(apiLoginId,apiTransactionKey,customerId)
    data = {
        "status": False,
        "successValue": None,
        "errorMessage": None
    }
    if result is not None:
      if result.messages.resultCode == "Ok":
        data={
            "status":True,
            "successValue":"OK",
            "errorMessage":None
           }
      else:
        data = {
              "status": False,
              "successValue": None,
              "errorMessage": str(result.messages.message[0]['text'].text)
        }
    print('End get_customer_profile')
    return jsonify(data)





if __name__ == '__main__':
    app.run(debug= True)
   # app.run(host="10.173.126.46", port=5000)