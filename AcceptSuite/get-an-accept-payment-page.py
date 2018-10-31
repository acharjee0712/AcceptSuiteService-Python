import os, sys
import imp

from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from authorizenet import constants
from decimal import *

def get_an_accept_payment_page(apiLoginId, apiTransactionKey, hostedPaymentIFrameCommunicatorUrl,customerId= None):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = apiLoginId
    merchantAuth.transactionKey = apiTransactionKey

    setting1 = apicontractsv1.settingType()
    setting1.settingName = apicontractsv1.settingNameEnum.hostedPaymentButtonOptions
    setting1.settingValue = "{\"text\": \"Pay\"}"

    setting2 = apicontractsv1.settingType()
    setting2.settingName = apicontractsv1.settingNameEnum.hostedPaymentOrderOptions
    setting2.settingValue = "{\"show\": false}"

    setting3 = apicontractsv1.settingType()
    setting3.settingName = apicontractsv1.settingNameEnum.hostedPaymentIFrameCommunicatorUrl
    setting3.settingValue = "{\"url\": \"" + hostedPaymentIFrameCommunicatorUrl + "\"}"

    setting4 = apicontractsv1.settingType()
    setting4.settingName = apicontractsv1.settingNameEnum.hostedPaymentBillingAddressOptions
    setting4.settingValue = "{\"show\": false}"

    setting5 = apicontractsv1.settingType()
    setting5.settingName = apicontractsv1.settingNameEnum.hostedPaymentReturnOptions
    setting5.settingValue = "{\"showReceipt\": false,\"url\":\"" + hostedPaymentIFrameCommunicatorUrl + "\",\"urlText\":\"Continue\",\"cancelUrlText\":\"Cancel\"}"


    settings = apicontractsv1.ArrayOfSetting()
    settings.setting.append(setting1)
    settings.setting.append(setting2)
    settings.setting.append(setting3)
    settings.setting.append(setting4)
    settings.setting.append(setting5)

    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = "authCaptureTransaction"
    transactionrequest.amount = 99

    if customerId is not None:
       if customerId != '':
         custprofile = apicontractsv1.customerProfilePaymentType()
         custprofile.customerProfileId = customerId
         transactionrequest.profile =custprofile

    paymentPageRequest = apicontractsv1.getHostedPaymentPageRequest()
    paymentPageRequest.merchantAuthentication = merchantAuth
    paymentPageRequest.transactionRequest = transactionrequest
    paymentPageRequest.hostedPaymentSettings = settings

    paymentPageController = getHostedPaymentPageController(paymentPageRequest)

    paymentPageController.execute()

    paymentPageResponse = paymentPageController.getresponse()

    if paymentPageResponse is not None:
        if paymentPageResponse.messages.resultCode == apicontractsv1.messageTypeEnum.Ok:
            print('Successfully got hosted payment page!')

            print('Token : %s' % paymentPageResponse.token)

            if paymentPageResponse.messages is not None:
                print('Message Code : %s' % paymentPageResponse.messages.message[0]['code'].text)
                print('Message Text : %s' % paymentPageResponse.messages.message[0]['text'].text)
        else:
            if paymentPageResponse.messages is not None:
                print('Failed to get batch statistics.\nCode:%s \nText:%s' % (paymentPageResponse.messages.message[0]['code'].text,paymentPageResponse.messages.message[0]['text'].text))

    return paymentPageResponse

#if(os.path.basename(__file__) == os.path.basename(sys.argv[0])):
  #  get_hosted_payment_page(constants.amount)
