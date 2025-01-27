#### getVelocity()


 uint8 MidiMessage::getVelocity ( ) const noexcept 
 

Returns the velocity of a noteon or noteoff message.The value returned will be in the range 0 to 127. If the message isn't a noteon or off event, it will return 0.See alsogetFloatVelocity