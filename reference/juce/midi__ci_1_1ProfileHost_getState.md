#### getState()


 SupportedAndActive midi\_ci::ProfileHost::getState ( ProfileAtAddress profileAtAddress ) const 
 

Returns the number of supported and active channels for the given profile on the specified group/channel.If the supported channels is 0, then the profile is not supported on the group/channel.If the active channels is 0, then the profile is inactive on the group/channel.References midi\_ci::ProfileAtAddress::address, midi\_ci::BlockProfileStates::getStateForDestination(), and midi\_ci::ProfileAtAddress::profile.