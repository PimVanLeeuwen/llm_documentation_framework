#### postSystemNotification()


 static void AccessibilityHandler::postSystemNotification ( const String & notificationTitle, const String & notificationBody ) static 
 

Posts a local system notification.In order for this to do anything, the following conditions must be met.At build time:The juce\_gui\_extra module must be included in the project.Push notifications must be enabled by setting the preprocessor definition JUCE\_PUSH\_NOTIFICATIONS=1At run time:An accessibility client (narrator, voiceover etc.) must be active.Additionally, on Android, an icon is required for notifications. This must be specified by adding the path to the icon file called "accessibilitynotificationicon" in the "Extra Android Raw Resources" setting in the Projucer.This will use the push notification client on macOS, iOS and Android. On Windows this will create a system tray icon to post the notification.Parameters

 notificationTitle the title of the notification 
 
 notificationBody the main body text of the notification