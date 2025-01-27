#### deliveredNotificationsListReceived()


 virtual void PushNotifications::Listener::deliveredNotificationsListReceived ( const Array< Notification > & notifications ) virtual 
 

Called after getDeliveredNotifications() request is fulfilled.Returns notifications that are visible in the notification area on the device and that are still waiting for a user action/response.On iOS, iOS version 10 or higher is required. On Android, API level 18 or higher is required. For unsupported platforms, an empty array will be returned.