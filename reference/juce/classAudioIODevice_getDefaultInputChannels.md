#### getDefaultInputChannels()


 virtual std::optional< BigInteger > AudioIODevice::getDefaultInputChannels ( ) const virtual 
 

For devices that support a default layout, returns the channels that are enabled in the default layout.Returns nullopt if the device doesn't supply a default layout.