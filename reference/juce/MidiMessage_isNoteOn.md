#### isNoteOn()


 bool MidiMessage::isNoteOn ( bool returnTrueForVelocity0 = false ) const noexcept 
 

Returns true if this message is a 'keydown' event.Parameters

 returnTrueForVelocity0 if true, then if this event is a noteon with velocity 0, it will still be considered to be a noteon and the method will return true. If returnTrueForVelocity0 is false, then if this is a noteon event with velocity 0, it'll be regarded as a noteoff, and the method will return false 
 



See alsoisNoteOff, getNoteNumber, getVelocity, noteOn