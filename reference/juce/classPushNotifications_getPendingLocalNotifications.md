#### getPendingLocalNotifications()


 void PushNotifications::getPendingLocalNotifications ( ) const 
 

iOS only: sends an asynchronous request to retrieve a list of notifications that were scheduled and not yet delivered.When the list is retrieved, Listener::pendingLocalNotificationsListReceived() will be called.