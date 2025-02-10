#### handleNoteOn()


 virtual void MidiKeyboardState::Listener::handleNoteOn ( MidiKeyboardState \* source, int midiChannel, int midiNoteNumber, float velocity ) pure virtual 
 

Called when one of the MidiKeyboardState's keys is pressed.This will be called synchronously when the state is either processing a buffer in its MidiKeyboardState::processNextMidiBuffer() method, or when a note is being played with its MidiKeyboardState::noteOn() method.Note that this callback could happen from an audio callback thread, so be careful not to block, and avoid any UI activity in the callback.Implemented in MidiMessageCollector.