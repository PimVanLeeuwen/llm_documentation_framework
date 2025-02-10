#### mono()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::mono ( ) static 
 

Creates a onechannel mono set (centre).Is equivalent to: kMonoAAX (VST), AAX\_eStemFormat\_Mono (AAX), kAudioChannelLayoutTag\_Mono (CoreAudio)Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().