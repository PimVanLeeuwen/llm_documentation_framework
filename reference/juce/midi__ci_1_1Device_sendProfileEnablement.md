#### sendProfileEnablement()


 void midi\_ci::Device::sendProfileEnablement ( MUID muid, 
 
 ChannelInGroup address, 
 Profile profile, 
 int numChannels ) 

Sets a profile on or off.Pass 0 or less to disable the profile, or a positive number to enable it.This also goes for group/block profiles. If the request is addressed to a group/block, then a positive number will cause a "profile on" message to be sent, and a nonpositive number will cause a "profile off" message to be sent. The channel count of the sent message will always be zero for messages addressed to groups/blocks.regardless of the value of the numChannels argument.