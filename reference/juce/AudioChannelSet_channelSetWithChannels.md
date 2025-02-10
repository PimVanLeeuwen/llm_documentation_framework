#### channelSetWithChannels()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::channelSetWithChannels ( const Array< ChannelType > & ) static 
 

Creates a channel set for a list of channel types.This function will assert if you supply a duplicate channel.Note that this method ignores the order in which the channels are given, i.e. two arrays with the same elements but in a different order will still result in the same channel set.