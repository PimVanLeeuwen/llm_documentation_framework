#### getPitchWheelValue()


 int MidiMessage::getPitchWheelValue ( ) const noexcept 
 

Returns the pitch wheel position from a pitchwheel move message.The value returned is a 14bit number from 0 to 0x3fff, indicating the wheel position. If called for messages which aren't pitch wheel events, the number returned will be nonsense.See alsoisPitchWheel