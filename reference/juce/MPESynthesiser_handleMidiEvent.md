#### handleMidiEvent()


 void MPESynthesiser::handleMidiEvent ( const MidiMessage & ) overridevirtual 
 

Handle incoming MIDI events.This method will be called automatically according to the MIDI data passed into renderNextBlock(), but you can also call it yourself to manually inject MIDI events.This implementation forwards program change messages and nonMPErelated controller messages to handleProgramChange and handleController, respectively, and then simply calls through to MPESynthesiserBase::handleMidiEvent to deal with MPErelated MIDI messages used for MPE notes, zones etc.This method can be overridden further if you need to do custom MIDI handling on top of what is provided here.Reimplemented from MPESynthesiserBase.