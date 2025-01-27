#### deviceTokenRefreshed()


 virtual void PushNotifications::Listener::deviceTokenRefreshed ( const String & token ) virtual 
 

Called whenever a token gets refreshed.You should monitor any token updates, because only the last token that is assigned to device is valid and can be used.