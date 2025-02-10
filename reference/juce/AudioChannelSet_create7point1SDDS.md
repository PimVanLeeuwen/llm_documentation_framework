#### create7point1SDDS()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::create7point1SDDS ( ) static 
 

Creates a set for a 7.1 surround setup (left, right, centre, leftSurround, rightSurround, leftCentre, rightCentre, LFE).Is equivalent to: k71Cine (VST), AAX\_eStemFormat\_7\_1\_SDDS (AAX), kAudioChannelLayoutTag\_MPEG\_7\_1\_A (CoreAudio)This format is referred to as "7.1 (SDDS)" in Logic Pro. This format is referred to as "7.1 SDDS" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().