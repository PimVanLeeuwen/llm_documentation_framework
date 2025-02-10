#### keySignatureMetaEvent()


 static MidiMessage MidiMessage::keySignatureMetaEvent ( int numberOfSharpsOrFlats, bool isMinorKey ) static 
 

Creates a keysignature metaevent.Parameters

 numberOfSharpsOrFlats if positive, this indicates the number of sharps in the key; if negative, the number of flats 
 
 isMinorKey if true, the key is minor; if false, it is major 



See alsoisKeySignatureMetaEvent