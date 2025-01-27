#### isMemberChannel()


 bool MPEInstrument::isMemberChannel ( int midiChannel ) const noexcept 
 

Returns true if the given MIDI channel (116) is a note channel in any of the MPEInstrument's MPE zones; false otherwise.When in legacy mode, this will return true if the given channel is contained in the current legacy mode channel range; false otherwise.