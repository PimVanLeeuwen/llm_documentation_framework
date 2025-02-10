#### getDefaultDeviceIndex()


 virtual int AudioIODeviceType::getDefaultDeviceIndex ( bool forInput ) const pure virtual 
 

Returns the name of the default device.This will be one of the names from the getDeviceNames() list.Parameters

 forInput if true, this means that a default input device should be returned; if false, it should return the default output