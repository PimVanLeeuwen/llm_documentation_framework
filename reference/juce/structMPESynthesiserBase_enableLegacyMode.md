#### enableLegacyMode()


 void MPESynthesiserBase::enableLegacyMode ( int pitchbendRange = 2, 
 
 Range< int > channelRange = Range< int >(1, 17) ) 

Puts the synthesiser into legacy mode.Parameters

 pitchbendRange The note pitchbend range in semitones to use when in legacy mode. Must be between 0 and 96, otherwise behaviour is undefined. The default pitchbend range in legacy mode is +/ 2 semitones. 
 
 channelRange The range of MIDI channels to use for notes when in legacy mode. The default is to use all MIDI channels (116). 


To get out of legacy mode, set a new MPE zone layout using setZoneLayout.