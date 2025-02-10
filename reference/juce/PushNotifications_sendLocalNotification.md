#### sendLocalNotification()


 void PushNotifications::sendLocalNotification ( const Notification & notification ) 
 

On iOS as well as on Android, sends a local notification.This will refresh an existing notification if the same identifier is used as in a notification that was already sent and not yet responded by a user.