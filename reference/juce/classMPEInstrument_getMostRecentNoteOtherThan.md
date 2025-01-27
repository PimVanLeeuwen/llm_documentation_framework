#### getMostRecentNoteOtherThan()


 MPENote MPEInstrument::getMostRecentNoteOtherThan ( MPENote otherThanThisNote ) const noexcept 
 

Returns the most recent note that is not the note passed in.If there is no such note, this returns an invalid MPENote (check with note.isValid() before use!).This helper method might be useful for some custom voice handling algorithms.