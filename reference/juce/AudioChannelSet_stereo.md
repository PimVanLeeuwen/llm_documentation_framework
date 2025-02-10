#### stereo()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::stereo ( ) static 
 

Creates a set containing a stereo set (left, right).Is equivalent to: kStereo (VST), AAX\_eStemFormat\_Stereo (AAX), kAudioChannelLayoutTag\_Stereo (CoreAudio)Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().