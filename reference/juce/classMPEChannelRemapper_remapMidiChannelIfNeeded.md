#### remapMidiChannelIfNeeded()


 void MPEChannelRemapper::remapMidiChannelIfNeeded ( MidiMessage & message, uint32 mpeSourceID ) noexcept 
 

Remaps the MIDI channel of the specified MIDI message (if necessary).Note that the MidiMessage object passed in will have it's channel changed if it needs to be remapped.Parameters

 message the message to be remapped 
 
 mpeSourceID the ID of the MPE source of the message. This is up to the user to define and keep constant