#### setTicksPerQuarterNote()


 void MidiFile::setTicksPerQuarterNote ( int ticksPerQuarterNote ) noexcept 
 

Sets the time format to use when this file is written to a stream.If this is called, the file will be written as bars/beats using the specified resolution, rather than SMPTE absolute times, as would be used if setSmpteTimeFormat() had been called instead.Parameters

 ticksPerQuarterNote e.g. 96, 960 
 



See alsosetSmpteTimeFormat