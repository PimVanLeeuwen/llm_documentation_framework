#### noteOn() [2/2]


 static MidiMessage MidiMessage::noteOn ( int channel, int noteNumber, uint8 velocity ) staticnoexcept 
 

Creates a keydown message (using an integer velocity).Parameters

 channel the midi channel, in the range 1 to 16 
 
 noteNumber the key number, 0 to 127 
 velocity in the range 0 to 127 



See alsoisNoteOn