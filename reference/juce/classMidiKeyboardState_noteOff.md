#### noteOff()


 void MidiKeyboardState::noteOff ( int midiChannel, 
 
 int midiNoteNumber, 
 float velocity ) 

Turns a specified note off.This will cause a suitable midi noteoff event to be injected into the midi buffer during the next call to processNextMidiBuffer().It will also trigger a synchronous callback to the listeners to tell them that the key has gone up.But if the note isn't actually down for the given channel, this method will in fact do nothing.