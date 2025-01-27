#### reset()


 void MidiKeyboardState::reset ( ) 
 

Resets the state of the object.All internal data for all the channels is reset, but no events are sent as a result.If you want to release any keys that are currently down, and to send out noteup midi messages for this, use the allNotesOff() method instead.