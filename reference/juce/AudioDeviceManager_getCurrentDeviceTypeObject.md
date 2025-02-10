#### getCurrentDeviceTypeObject()


 AudioIODeviceType \* AudioDeviceManager::getCurrentDeviceTypeObject ( ) const 
 

Returns the currently active audio device type object.Don't keep a copy of this pointer it's owned by the device manager and could change at any time.