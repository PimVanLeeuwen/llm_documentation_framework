#### getNumPropertyExchangeRequestsSupportedForMuid()


 std::optional< int > midi\_ci::Device::getNumPropertyExchangeRequestsSupportedForMuid ( MUID m ) const 
 

Returns the number of simultaneous property exchange requests supported by a particular device.If there's no record of this device's property capabilities (including the case where the device doesn't support property exchange at all) this will return nullopt.Devices don't report property capabilities unless asked; you can request capabilities using inquirePropertyCapabilities().