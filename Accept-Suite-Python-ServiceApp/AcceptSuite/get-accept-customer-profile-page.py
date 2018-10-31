import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from authorizenet import constants
from decimal import *

def get_accept_customer_profile_page(apiLoginId, apiTransactionKey, hostedProfileIFrameCommunicatorUrl,customerId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = apiLoginId
    merchantAuth.transactionKey = apiTransactionKey

    setting = apicontractsv1.settingType()
    setting.settingName = apicontractsv1.settingNameEnum.hostedProfileIFrameCommunicatorUrl
    setting.settingValue = hostedProfileIFrameCommunicatorUrl

    settings = apicontractsv1.ArrayOfSetting()
    settings.setting.append(setting)

    profilePageRequest = apicontractsv1.getHostedProfilePageRequest()
    profilePageRequest.merchantAuthentication = merchantAuth
    profilePageRequest.customerProfileId = customerId
    profilePageRequest.hostedProfileSettings = settings

    profilePageController = getHostedProfilePageController(profilePageRequest)

    profilePageController.execute()

    profilePageResponse = profilePageController.getresponse()

    if profilePageResponse is not None:
        if profilePageResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got hosted profile page!')

            print('Token : %s' % profilePageResponse.token)

            if profilePageResponse.messages:
                print('Message Code : %s' % profilePageResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % profilePageResponse.messages.message[0]['text'].text)
        else:
            if profilePageResponse.messages:
                print('Failed to get batch statistics.\nCode:%s \nText:%s' % (profilePageResponse.messages.message[0]['code'].text,profilePageResponse.messages.message[0]['text'].text))

    return profilePageResponse

#if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
    #get_hosted_profile_page(constants.customerProfileId)
