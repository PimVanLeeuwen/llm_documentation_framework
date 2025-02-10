#### noteOn()


 void MidiKeyboardState::noteOn ( int midiChannel, 
 
 int midiNoteNumber, 
 float velocity ) 

Turns a specified note on.This will cause a suitable midi noteon event to be injected into the midi buffer during the next call to processNextMidiBuffer().It will also trigger a synchronous callback to the listeners to tell them that the key has gone down.