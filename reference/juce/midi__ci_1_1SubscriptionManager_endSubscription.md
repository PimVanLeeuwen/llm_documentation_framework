#### endSubscription()


 void midi\_ci::SubscriptionManager::endSubscription ( SubscriptionKey ) 
 

Ends an ongoing subscription by us.If the subscription begin request hasn't been sent yet, then this will just cancel the cached request.If a subscription begin request has been sent, but no response has been received, this will send a notification cancelling the initial request via SubscriptionManagerDelegate::abortPropertyRequest().If the subscription has started successfully, then this will send a subscription end request via SubscriptionManagerDelegate::sendPropertySubscribe().