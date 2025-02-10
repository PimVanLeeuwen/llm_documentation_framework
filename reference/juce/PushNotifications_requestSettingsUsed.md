#### requestSettingsUsed()


 void PushNotifications::requestSettingsUsed ( ) 
 

Sends an asynchronous request to retrieve current settings that are currently in use.These can be exactly the same as used in requestPermissionsWithSettings(), but depending on user's subsequent changes in OS settings, the actual current settings may be different (e.g. user might have later decided to disable sounds).Note that settings are currently only used on iOS and partially on OSX.On OSX, only allow\* flags are used and they refer to remote notifications only. For local notifications, refer to System Preferences.When calling this function on other platforms, Settings with no categories and all allow\* flags set to true will be received in Listener::notificationSettingsReceived().