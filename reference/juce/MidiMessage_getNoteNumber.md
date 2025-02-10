#### getNoteNumber()


 int MidiMessage::getNoteNumber ( ) const noexcept 
 

Returns the midi note number for noteon and noteoff messages.If the message isn't a noteon or off, the value returned is undefined.See alsoisNoteOff, getMidiNoteName, getMidiNoteInHertz, setNoteNumber