#### setSmpteTimeFormat()


 void MidiFile::setSmpteTimeFormat ( int framesPerSecond, int subframeResolution ) noexcept 
 

Sets the time format to use when this file is written to a stream.If this is called, the file will be written using absolute times, rather than bars/beats as would be the case if setTicksPerBeat() had been called instead.Parameters

 framesPerSecond must be 24, 25, 29 or 30 
 
 subframeResolution the subsecond resolution, e.g. 4 (midi time code), 8, 10, 80 (SMPTE bit resolution), or 100. For millisecond timing, setSmpteTimeFormat (25, 40) 



See alsosetTicksPerBeat