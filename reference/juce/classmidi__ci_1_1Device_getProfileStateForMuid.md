#### getProfileStateForMuid()


 const ChannelProfileStates \* midi\_ci::Device::getProfileStateForMuid ( MUID m, 
 
 ChannelAddress address ) const 

Returns the states of the profiles on a particular channel of a device.If the state is unknown, returns nullptr.Devices don't report profile capabilities unless asked; you can request capabilities using inquireProfile().