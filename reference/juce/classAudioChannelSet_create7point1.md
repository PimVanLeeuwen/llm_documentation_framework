#### create7point1()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create7point1 ( ) static 
 

Creates a set for a DTS 7.1 surround setup (left, right, centre, leftSurroundSide, rightSurroundSide, leftSurroundRear, rightSurroundRear, LFE).Is equivalent to: k71CineSideFill (VST), AAX\_eStemFormat\_7\_1\_DTS (AAX), kAudioChannelLayoutTag\_MPEG\_7\_1\_C/kAudioChannelLayoutTag\_ITU\_3\_4\_1 (CoreAudio)This format is referred to as "7.1 (3/4.1)" in Logic Pro. This format is referred to as "7.1" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().