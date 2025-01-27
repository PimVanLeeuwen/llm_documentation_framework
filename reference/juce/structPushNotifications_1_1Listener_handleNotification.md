#### handleNotification()


 virtual void PushNotifications::Listener::handleNotification ( bool isLocalNotification, const Notification & notification ) virtual 
 

This can be called in multiple different situations, depending on the OS and the situation.This will be called when a user presses on a notificationNote: On Android, if remote notification was received while the app was in the background and then user pressed on it, the notification object received in this callback will contain only "properties" member set. Hence, if you want to know what was the notification title, content etc, you need to set them as additional properties, so that you will be able to restore them from "properties" dictionary.Note you can receive this callback on startup, if the application was launched from a notification.