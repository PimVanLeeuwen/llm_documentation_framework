#### setVelocity()


 void MidiMessage::setVelocity ( float newVelocity ) noexcept 
 

Changes the velocity of a noteon or noteoff message.If the message isn't a note on or off, this will do nothing.Parameters

 newVelocity the new velocity, in the range 0 to 1.0 
 



See alsogetFloatVelocity, multiplyVelocity