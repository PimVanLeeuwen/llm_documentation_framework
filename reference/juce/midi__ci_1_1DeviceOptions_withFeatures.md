#### withFeatures()


 DeviceOptions midi\_ci::DeviceOptions::withFeatures ( DeviceFeatures x ) const nodiscard 
 

The features that you want to enable on the device.If you enable property exchange, you may wish to supply a PropertyDelegate using withPropertyDelegate(). If you enable profile configuration, you may wish to supply a ProfileDelegate using withProfileDelegate(). Process inquiry is not currently supported.References withMember(), and x.