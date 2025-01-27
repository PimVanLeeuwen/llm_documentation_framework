#### remoteNotificationsDeleted()


 virtual void PushNotifications::Listener::remoteNotificationsDeleted ( ) virtual 
 

Called when Firebase Cloud Messaging server deletes pending messages.This can happen when 1) too many messages were sent to the server (hint: use collapsible messages). 2) the devices hasn't been online in a long time (refer to Firebase documentation for the maximum time a message can be stored on FCM before expiring).