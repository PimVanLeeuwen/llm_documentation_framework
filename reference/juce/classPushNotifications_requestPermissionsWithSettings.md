#### requestPermissionsWithSettings()


 void PushNotifications::requestPermissionsWithSettings ( const Settings & settings ) 
 

Initialises push notifications on current device with the settings provided.Call this on your application startup and on iOS the first time the application starts, a user will be presented with a permission request dialog to give push notifications permission. Once a user responds, Listener::notificationSettingsReceived() will be called so that you can check what permissions where actually granted. The listener callback will be called on each subsequent startup too (provided you called requestPermissionsWithSettings() on previous application run). This way you can check what are current push notifications permissions.Note that settings are currently only used on iOS. When calling on other platforms, Settings with no categories and all allow\* flags set to true will be received in Listener::notificationSettingsReceived().You can also call requestSettingsUsed() to explicitly ask for current settings.