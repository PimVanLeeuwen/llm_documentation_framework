#### quadraphonic()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::quadraphonic ( ) static 
 

Creates a set for quadraphonic surround setup (left, right, leftSurround, rightSurround)Is equivalent to: k40Music (VST), AAX\_eStemFormat\_Quad (AAX), kAudioChannelLayoutTag\_Quadraphonic (CoreAudio)This format is referred to as "Quadraphonic" in Logic Pro. This format is referred to as "Quadro" in Cubase. This format is referred to as "Quad" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().