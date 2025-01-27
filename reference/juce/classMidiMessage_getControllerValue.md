#### getControllerValue()


 int MidiMessage::getControllerValue ( ) const noexcept 
 

Returns the controller value from a controller message.A value 0 to 127 is returned to indicate the new controller position. Note that the value returned is invalid for messages that aren't controller changes.See alsoisController, getControllerNumber