#### ambisonic()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::ambisonic ( int order = 1 ) static 
 

Creates a set for ACN, SN3D normalised ambisonic surround setups with a given order.Is equivalent to: kAmbiXXXOrderACN (VST), AAX\_eStemFormat\_Ambi\_XXX\_ACN (AAX), kAudioChannelLayoutTag\_HOA\_ACN\_SN3D (CoreAudio)