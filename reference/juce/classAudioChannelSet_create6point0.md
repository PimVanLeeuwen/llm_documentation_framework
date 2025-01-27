#### create6point0()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create6point0 ( ) static 
 

Creates a set for a 6.0 Cine surround setup (left, right, centre, leftSurround, rightSurround, centreSurround).Is equivalent to: k60Cine (VST), AAX\_eStemFormat\_6\_0 (AAX), kAudioChannelLayoutTag\_AudioUnit\_6\_0 (CoreAudio)Logic Pro incorrectly uses this for the surround format labeled "6.1 (ES/EX)". This format is referred to as "6.0 Cine" in Cubase. This format is referred to as "6.0" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().