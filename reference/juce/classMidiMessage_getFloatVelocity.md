#### getFloatVelocity()


 float MidiMessage::getFloatVelocity ( ) const noexcept 
 

Returns the velocity of a noteon or noteoff message.The value returned will be in the range 0 to 1.0 If the message isn't a noteon or off event, it will return 0.See alsogetVelocity, setVelocity