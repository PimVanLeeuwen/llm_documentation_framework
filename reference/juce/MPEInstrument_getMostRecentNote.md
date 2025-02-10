#### getMostRecentNote()


 MPENote MPEInstrument::getMostRecentNote ( int midiChannel ) const noexcept 
 

Returns the most recent note that is playing on the given midiChannel (this will be the note which has received the most recent noteon without a corresponding noteoff), if there is such a note.Otherwise, this returns an invalid MPENote (check with note.isValid() before use!)