import os, sys
import imp
 
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *

 
def get_customer_profile(apiLoginId, apiTransactionKey,customerProfileId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = apiLoginId
    merchantAuth.transactionKey = apiTransactionKey
 
    getCustomerProfile = apicontractsv1.getCustomerProfileRequest()
    getCustomerProfile.merchantAuthentication = merchantAuth
    getCustomerProfile.customerProfileId = customerProfileId
    controller = getCustomerProfileController(getCustomerProfile)
    controller.execute()
 
    response = controller.getresponse()
 
    if (response.messages.resultCode=="Ok"):
        print ("Successfully retrieved a customer with profile ")

    else:
        print ("response code: %s" % response.messages.resultCode)
        print ("Failed to get customer profile information with id %s" % getCustomerProfile.customerProfileId)

    return response
 
#if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
   # get_customer_profile(constants.customerProfileId)