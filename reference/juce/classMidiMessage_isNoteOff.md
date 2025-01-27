#### isNoteOff()


 bool MidiMessage::isNoteOff ( bool returnTrueForNoteOnVelocity0 = true ) const noexcept 
 

Returns true if this message is a 'keyup' event.If returnTrueForNoteOnVelocity0 is true, then his will also return true for a noteon event with a velocity of 0.See alsoisNoteOn, getNoteNumber, getVelocity, noteOff