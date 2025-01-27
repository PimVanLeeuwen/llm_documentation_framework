#### beginSubscription()


 SubscriptionKey midi\_ci::SubscriptionManager::beginSubscription ( MUID m, 
 
 const PropertySubscriptionHeader & header ) 

Attempts to begin a subscription using the provided details.Returnsa token that uniquely identifies this subscription. This token can be passed to endSubscription to terminate an ongoing subscription.