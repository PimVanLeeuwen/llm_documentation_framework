#### upstreamMessageSent()


 virtual void PushNotifications::Listener::upstreamMessageSent ( const String & messageId ) virtual 
 

Called when an upstream message sent with PushNotifications::sendUpstreamMessage() has been sent successfully.Bear in mind that in may take several minutes or more to receive this callback.