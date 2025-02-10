#### sendSubscriptionUpdate()


 std::optional< RequestKey > midi\_ci::PropertyHost::sendSubscriptionUpdate ( MUID device, 
 
 const PropertySubscriptionHeader & header, 
 Span< const std::byte > body, 
 std::function< void(const PropertyExchangeResult &)> callback ) 

Sends a "Subscription" message from a device, when acting as a subscription responder.You should call this for all registered subscribers whenever the subscribed property is modified in a way that remote devices don't know about (if a remote device requests a property update, there's no need to send a subscription update after changing the property accordingly).You should not attempt to start a new subscription on another device using this function. Valid subscription commands are "full", "partial", and "notify". Check the property exchange specification for the intended use of these commands.To terminate a subscription that was initiated by a remote device, use terminateSubscription().The provided callback will be called once the remote device has confirmed receipt of the subscription update. If the state of your application changes such that you no longer need to respond/wait for confirmation, you can pass the request key to Device::abortPropertyRequest().