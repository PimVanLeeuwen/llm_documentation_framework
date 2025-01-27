#### getAfterTouchValue()


 int MidiMessage::getAfterTouchValue ( ) const noexcept 
 

Returns the amount of aftertouch from an aftertouch messages.The value returned is in the range 0 to 127, and will be nonsense for messages other than aftertouch messages.See alsoisAftertouch