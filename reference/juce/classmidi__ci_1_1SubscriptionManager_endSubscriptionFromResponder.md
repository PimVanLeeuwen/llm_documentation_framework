#### endSubscriptionFromResponder()


 void midi\_ci::SubscriptionManager::endSubscriptionFromResponder ( MUID , 
 
 String ) 

Ends an ongoing subscription as requested from the remote device.Unlike the other overload of endSubscription, this won't notify the delegate. It will only update the internal record of active subscriptions.Calls Delegate::propertySubscriptionChanged().