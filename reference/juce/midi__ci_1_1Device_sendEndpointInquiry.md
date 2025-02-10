#### sendEndpointInquiry()


 void midi\_ci::Device::sendEndpointInquiry ( MUID destination, 
 
 Message::EndpointInquiry endpoint ) 

Sends an endpoint inquiry message.Check the MIDICI spec for an explanation of the different endpoint message status codes.Received responses will be sent to DeviceListener::endpointReceived. Responses are not cached by the Device; if you need to cache endpoint responses, you can keep your own map of MUID>response, update it in endpointReceived, and remove entries in DeviceListener::deviceRemoved.