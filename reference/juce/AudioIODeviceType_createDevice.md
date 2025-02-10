#### createDevice()


 virtual AudioIODevice \* AudioIODeviceType::createDevice ( const String & outputDeviceName, const String & inputDeviceName ) pure virtual 
 

Creates one of the devices of this type.The deviceName must be one of the strings returned by getDeviceNames(), and scanForDevices() must have been called before this method is used.