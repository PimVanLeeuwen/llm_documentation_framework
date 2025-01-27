#### sendProfileDetailsInquiry()


 void midi\_ci::Device::sendProfileDetailsInquiry ( MUID muid, 
 
 ChannelInGroup address, 
 Profile profile, 
 std::byte target ) 

Sends a profile details inquiry to a particular device.DeviceListener::profileDetailsReceived will be called when the device replies.