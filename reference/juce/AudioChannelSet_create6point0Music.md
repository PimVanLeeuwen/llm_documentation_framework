#### create6point0Music()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create6point0Music ( ) static 
 

Creates a set for a 6.0 Music surround setup (left, right, leftSurround, rightSurround, leftSurroundSide, rightSurroundSide).Is equivalent to: k60Music (VST), n/a (AAX), kAudioChannelLayoutTag\_DTS\_6\_0\_A (CoreAudio)This format is referred to as "6.0 Music" in Cubase.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().