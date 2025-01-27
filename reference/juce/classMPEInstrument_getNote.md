#### getNote() [2/2]


 MPENote MPEInstrument::getNote ( int midiChannel, int midiNoteNumber ) const noexcept 
 

Returns the note currently playing on the given midiChannel with the specified initial MIDI note number, if there is such a note.Otherwise, this returns an invalid MPENote (check with note.isValid() before use!)