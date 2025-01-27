#### notificationSettingsReceived()


 virtual void PushNotifications::Listener::notificationSettingsReceived ( const Settings & settings ) virtual 
 

This callback will be called after you call requestSettingsUsed() or requestPermissionsWithSettings().Note that settings are currently only used on iOS. When called on other platforms, Settings with no categories and all allow flags set to true will be received in Listener::notificationSettingsReceived().