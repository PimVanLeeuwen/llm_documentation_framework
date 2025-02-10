#### scanForDevices()


 virtual void AudioIODeviceType::scanForDevices ( ) pure virtual 
 

Refreshes the object's cached list of known devices.This must be called at least once before calling getDeviceNames() or any of the other device creation methods.