#### setNoteNumber()


 void MidiMessage::setNoteNumber ( int newNoteNumber ) noexcept 
 

Changes the midi note number of a noteon or noteoff message.If the message isn't a note on or off, this will do nothing.