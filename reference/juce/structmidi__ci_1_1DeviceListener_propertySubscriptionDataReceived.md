#### propertySubscriptionDataReceived()


 virtual void midi\_ci::DeviceListener::propertySubscriptionDataReceived ( MUID x, const PropertySubscriptionData & data ) virtual 
 

Called to indicate that a subscription update was received.This only receives messages with responder commands (partial, full, notify, end).To start a subscription, use Device::sendPropertySubscriptionStart().