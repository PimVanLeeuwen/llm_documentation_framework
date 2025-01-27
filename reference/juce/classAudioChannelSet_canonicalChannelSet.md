#### canonicalChannelSet()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::canonicalChannelSet ( int numChannels ) static 
 

Create a canonical channel set for a given number of channels.For example, numChannels = 1 will return mono, numChannels = 2 will return stereo, etc.