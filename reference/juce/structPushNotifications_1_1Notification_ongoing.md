#### ongoing


 bool PushNotifications::Notification::ongoing = false 
 

Optional: If true, then it cannot be dismissed by the user and it must be dismissed manually.Typically used for ongoing background tasks that the user is actively engaged with. To dismiss such notification, you need to call removeDeliveredNotification() or removeAllDeliveredNotifications().