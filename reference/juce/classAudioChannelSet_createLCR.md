#### createLCR()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::createLCR ( ) static 
 

Creates a set containing an LCR set (left, right, centre).Is equivalent to: k30Cine (VST), AAX\_eStemFormat\_LCR (AAX), kAudioChannelLayoutTag\_MPEG\_3\_0\_A (CoreAudio)This format is referred to as "LRC" in Cubase. This format is referred to as "LCR" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().