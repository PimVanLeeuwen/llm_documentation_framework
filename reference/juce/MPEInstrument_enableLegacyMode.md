#### enableLegacyMode()


 void MPEInstrument::enableLegacyMode ( int pitchbendRange = 2, 
 
 Range< int > channelRange = Range< int >(1, 17) ) 

Puts the instrument into legacy mode.If legacy mode is already enabled this method does nothing.As a side effect, this will discard all currently playing notes, and call noteReleased for all of them.This special zone layout mode is for backwards compatibility with nonMPE MIDI devices. In this mode, the instrument will ignore the current MPE zone layout. It will instead take a range of MIDI channels (default: all channels 116) and treat them as note channels, with no master channel. MIDI channels outside of this range will be ignored.Parameters

 pitchbendRange The note pitchbend range in semitones to use when in legacy mode. Must be between 0 and 96, otherwise behaviour is undefined. The default pitchbend range in legacy mode is +/ 2 semitones. 
 
 channelRange The range of MIDI channels to use for notes when in legacy mode. The default is to use all MIDI channels (116). 


To get out of legacy mode, set a new MPE zone layout using setZoneLayout.