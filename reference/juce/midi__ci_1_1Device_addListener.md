#### addListener()


 void midi\_ci::Device::addListener ( Listener & l ) 
 

Adds a listener that will be notified when particular events occur.Check the members of the Listener class to see the kinds of events that are reported. To receive notifications through Listener::propertySubscriptionReceived(), you must first request a subscription using sendPropertySubscriptionStart().See alsoListener, removeListener()