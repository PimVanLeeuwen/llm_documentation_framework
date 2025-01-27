#### create6point1Music()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create6point1Music ( ) static 
 

Creates a set for a 6.0 Music surround setup (left, right, leftSurround, rightSurround, leftSurroundSide, rightSurroundSide, LFE).Is equivalent to: k61Music (VST), n/a (AAX), kAudioChannelLayoutTag\_DTS\_6\_1\_A (CoreAudio)Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().