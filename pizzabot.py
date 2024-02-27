import json
 
def prepareResponse(event, msgText):
    response = {
          "sessionState": {
            "dialogAction": {
              "type": "Close"
            },
            "intent": {
              "name": event['sessionState']['intent']['name'],
                  "state": "Fulfilled"
            }
          },
          "messages": [
           {
             "contentType": "PlainText",
             "content": msgText
            }
           ]
       }
     
    return response
 
def CancelOrderIntent(event):
    msgText = "Order has been canceled"
    return prepareResponse(event, msgText)
 
def CreateOrderIntent(event):
     real_price=0
     cost=250
     #firstName = event['sessionState']['intent']['slots']['name']['value']['interpretedValue']
     pizzatype = event['sessionState']['intent']['slots']['type']['value']['interpretedValue']
     pizzasize = event['sessionState']['intent']['slots']['size']['value']['interpretedValue']
     discount = int(event['sessionState']['sessionAttributes']['discount'])
     if(pizzatype == "meatpizza" and pizzasize == "large"):
        real_price=400
        cost= real_price-(real_price*int(discount)/100)
     print(pizzasize,pizzatype)
     print('Discount: ', discount)
     # Your custom order creation code here.
      
     msgText = "Your Order for, " + str(pizzasize) + " " + str(pizzatype) +" Bill is:"+ str(cost) + " and your Order no is#: 342342"
     
     return prepareResponse(event, msgText)   
      
     
def lambda_handler(event, context):
    intentName = event['sessionState']['intent']['name']
    response = None
         
    if intentName == 'CreateOrderIntent':
        response = CreateOrderIntent(event)
    elif intentName == 'CancelOrderIntent':
        response = CancelOrderIntent(event)
    else: 
        raise Exception('The intent : ' + intentName + ' is not supported')
    return response
