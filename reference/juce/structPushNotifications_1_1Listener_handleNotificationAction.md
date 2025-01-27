#### handleNotificationAction()


 virtual void PushNotifications::Listener::handleNotificationAction ( bool isLocalNotification, const Notification & notification, const String & actionIdentifier, const String & optionalResponse ) virtual 
 

This can be called when a user performs some action on the notification such as pressing on an action button or responding with a text input.Note that pressing on a notification area, i.e. not on an action button is not considered to be an action, and hence receivedNotification() will be called in that case.Note you can receive this callback on startup, if the application was launched from a notification's action.Parameters

 isLocalNotification If the notification is local 
 
 notification The notification 
 actionIdentifier A String identifying the action 
 optionalResponse Text response a user inputs for notifications with a text input. Empty for notifications without a text input option.