#### multiplyVelocity()


 void MidiMessage::multiplyVelocity ( float scaleFactor ) noexcept 
 

Multiplies the velocity of a noteon or noteoff message by a given amount.If the message isn't a note on or off, this will do nothing.Parameters

 scaleFactor the value by which to multiply the velocity 
 



See alsosetVelocity