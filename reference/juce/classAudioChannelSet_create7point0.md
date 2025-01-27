#### create7point0()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create7point0 ( ) static 
 

Creates a set for a DTS 7.0 surround setup (left, right, centre, leftSurroundSide, rightSurroundSide, leftSurroundRear, rightSurroundRear).Is equivalent to: k70Music (VST), AAX\_eStemFormat\_7\_0\_DTS (AAX), kAudioChannelLayoutTag\_AudioUnit\_7\_0 (CoreAudio)This format is referred to as "7.0" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().