#### create5point0()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create5point0 ( ) static 
 

Creates a set for a 5.0 surround setup (left, right, centre, leftSurround, rightSurround).Is equivalent to: k50 (VST), AAX\_eStemFormat\_5\_0 (AAX), kAudioChannelLayoutTag\_MPEG\_5\_0\_A (CoreAudio)This format is referred to as "5.0" in Cubase. This format is referred to as "5.0" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().