#### create5point1()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create5point1 ( ) static 
 

Creates a set for a 5.1 surround setup (left, right, centre, leftSurround, rightSurround, LFE).Is equivalent to: k51 (VST), AAX\_eStemFormat\_5\_1 (AAX), kAudioChannelLayoutTag\_MPEG\_5\_1\_A (CoreAudio)This format is referred to as "5.1 (ITU 775)" in Logic Pro. This format is referred to as "5.1" in Cubase. This format is referred to as "5.1" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().