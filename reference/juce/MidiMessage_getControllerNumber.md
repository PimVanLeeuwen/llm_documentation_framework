#### getControllerNumber()


 int MidiMessage::getControllerNumber ( ) const noexcept 
 

Returns the controller number of a controller message.The name of the controller can be looked up using the getControllerName() method. Note that the value returned is invalid for messages that aren't controller changes.See alsoisController, getControllerName, getControllerValue