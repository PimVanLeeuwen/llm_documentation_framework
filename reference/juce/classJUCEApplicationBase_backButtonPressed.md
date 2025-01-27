#### backButtonPressed()


 virtual bool JUCEApplicationBase::backButtonPressed ( ) virtual 
 

This will be called when the back button on a device is pressed.The return value should be used to indicate whether the back button event has been handled by the application, for example if you want to implement custom navigation instead of the standard behaviour on Android.This is currently only implemented on Android devices.Returnstrue if the event has been handled, or false if the default OS behaviour should happen