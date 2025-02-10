#### namedChannelSet()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::namedChannelSet ( int numChannels ) static 
 

Create a channel set for a given number of channels which is nondiscrete.If numChannels is larger than the number of channels of the surround format with the maximum amount of channels (currently 7.1 Surround), then this function returns an empty set.