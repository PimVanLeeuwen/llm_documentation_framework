#### handleMidiEvent()


 virtual void MPESynthesiserBase::handleMidiEvent ( const MidiMessage & ) virtual 
 

Handle incoming MIDI events (called from renderNextBlock).The default implementation provided here simply forwards everything to MPEInstrument::processNextMidiEvent, where it is used to update the MPE notes, zones etc. MIDI messages not relevant for MPE are ignored.This method can be overridden if you need to do custom MIDI handling on top of MPE. The MPESynthesiser class overrides this to implement callbacks for MIDI program changes and nonMPErelated MIDI controller messages.Reimplemented in MPESynthesiser.