#### allNotesOff()


 void MidiKeyboardState::allNotesOff ( int midiChannel ) 
 

This will turn off any currentlydown notes for the given midi channel.If you pass 0 for the midi channel, it will in fact turn off all notes on all channels.Calling this method will make calls to noteOff(), so can trigger synchronous callbacks and events being added to the midi stream.