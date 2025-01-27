#### create6point1()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create6point1 ( ) static 
 

Creates a set for a 6.1 Cine surround setup (left, right, centre, leftSurround, rightSurround, centreSurround, LFE).Is equivalent to: k61Cine (VST), AAX\_eStemFormat\_6\_1 (AAX), kAudioChannelLayoutTag\_MPEG\_6\_1\_A (CoreAudio)This format is referred to as "6.1" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().