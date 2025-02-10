#### sendPropertyCapabilitiesInquiry()


 void midi\_ci::Device::sendPropertyCapabilitiesInquiry ( MUID destination ) 
 

Sends a property inquiry to a particular device.If the device supports properties, this will also automatically request the ResourceList property, and then the ChannelList and DeviceInfo properties if they are present in the ResourceList.