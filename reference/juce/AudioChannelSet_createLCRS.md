#### createLCRS()


 static AudioChannelSet JUCE\_CALLTYPE AudioChannelSet::createLCRS ( ) static 
 

Creates a set containing an LCRS set (left, right, centre, surround).Is equivalent to: k40Cine (VST), AAX\_eStemFormat\_LCRS (AAX), kAudioChannelLayoutTag\_MPEG\_4\_0\_A (CoreAudio)This format is referred to as "LCRS (Pro Logic)" in Logic Pro. This format is referred to as "LRCS" in Cubase. This format is referred to as "LCRS" in Pro Tools.Referenced by SpeakerMappings::channelSetToVstArrangementType(), and SpeakerMappings::vstArrangementTypeToChannelSet().