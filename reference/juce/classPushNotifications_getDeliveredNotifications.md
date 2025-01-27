#### getDeliveredNotifications()


 void PushNotifications::getDeliveredNotifications ( ) const 
 

Sends a request for a list of notifications delivered.Such notifications are visible in the notification area on the device and they are still waiting for user action/response. When the request is finished Listener::deliveredNotificationsListReceived() will be called.On iOS, iOS version 10 or higher is required. On Android, API level 18 or higher is required. For unsupported platforms, Listener::deliveredNotificationsListReceived() will return an empty array.