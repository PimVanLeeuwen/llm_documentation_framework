#### processNextMidiEvent()


 virtual void MPEInstrument::processNextMidiEvent ( const MidiMessage & message ) virtual 
 

Process a MIDI message and trigger the appropriate method calls (noteOn, noteOff etc.)You can override this method if you need some special MIDI message treatment on top of the standard MPE logic implemented here.