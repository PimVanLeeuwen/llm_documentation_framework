#### getDeviceToken()


 String PushNotifications::getDeviceToken ( ) const 
 

Retrieves current device token.Note, it is not a good idea to cache this token because it may change in the meantime. Always call this method to get the current token value.