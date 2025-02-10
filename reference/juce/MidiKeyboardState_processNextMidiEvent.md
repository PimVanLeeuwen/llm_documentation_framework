#### processNextMidiEvent()


 void MidiKeyboardState::processNextMidiEvent ( const MidiMessage & message ) 
 

Looks at a keyup/down event and uses it to update the state of this object.To process a buffer full of midi messages, use the processNextMidiBuffer() method instead.