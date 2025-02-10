#### isMasterChannel()


 bool MPEInstrument::isMasterChannel ( int midiChannel ) const noexcept 
 

Returns true if the given MIDI channel (116) is a master channel (channel 1 or 16).In legacy mode, this will always return false.