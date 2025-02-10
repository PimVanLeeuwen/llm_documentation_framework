#### create7point0SDDS()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create7point0SDDS ( ) static 
 

Creates a set for a SDDS 7.0 surround setup (left, right, centre, leftSurround, rightSurround, leftCentre, rightCentre).Is equivalent to: k70Cine (VST), AAX\_eStemFormat\_7\_0\_SDDS (AAX), kAudioChannelLayoutTag\_AudioUnit\_7\_0\_Front (CoreAudio)This format is referred to as "7.0 SDDS" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().