#### getProgramChangeNumber()


 int MidiMessage::getProgramChangeNumber ( ) const noexcept 
 

Returns the new program number of a program change message.If the message isn't a program change, the value returned is undefined.See alsoisProgramChange, getGMInstrumentName