#### getDeviceNames()


 virtual StringArray AudioIODeviceType::getDeviceNames ( bool wantInputNames = false ) const pure virtual 
 

Returns the list of available devices of this type.The scanForDevices() method must have been called to create this list.Parameters

 wantInputNames for devices which have separate inputs and outputs this determines which list of names is returned