#### createLRS()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::createLRS ( ) static 
 

Creates a set containing an LRS set (left, right, surround).Is equivalent to: k30Music (VST), n/a (AAX), kAudioChannelLayoutTag\_ITU\_2\_1 (CoreAudio)This format is referred to as "LRS" in Cubase.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().