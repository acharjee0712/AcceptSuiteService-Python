import imp

#!flask/bin/python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Accept JS / Accept UI

@app.route('/api/AcceptSuite/AcceptJS', methods=['GET'])
def get_AcceptJS():

    apiLoginId = request.args.get('apiLoginId')
    transactionKey = request.args.get('transactionKey')
    token = request.args.get('token')

    print('Start create_an_accept_payment_transaction')

    modl = imp.load_source('modulename', 'AcceptSuite/create-an-accept-payment-transaction.py')
    result= modl.create_an_accept_payment_transaction(apiLoginId,transactionKey,token)
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
    return jsonify({'data': data})


# Accept Hosted

@app.route('/api/AcceptSuite/AcceptHosted', methods=['GET'])
def get_AcceptHosted():

    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    iFrameCommunicatorUrl=request.args.get('iFrameCommunicatorUrl')
    customerId = request.args.get('customerId')
    print('Start get_an_accept_payment_page')

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
    return jsonify({'data': data})


# Accept Customer

@app.route('/api/AcceptSuite/AcceptCustomer', methods=['GET'])
def get_AcceptCustomer():

    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    iFrameCommunicatorUrl=request.args.get('iFrameCommunicatorUrl')
    customerId = request.args.get('customerId')
    print('Start get_accept_customer_profile_page')

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
    return jsonify({'data': data})


# Validate Customer

@app.route('/api/AcceptSuite/ValidateCustomer', methods=['GET'])
def get_ValidateCustomer():

    apiLoginId = request.args.get('apiLoginId')
    apiTransactionKey = request.args.get('apiTransactionKey')
    customerId = request.args.get('customerId')
    print('Start get_customer_profile')

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
    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(debug= True)
   # app.run(host="10.173.126.46", port=5000)