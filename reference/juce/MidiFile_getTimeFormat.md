#### getTimeFormat()


 short MidiFile::getTimeFormat ( ) const noexcept 
 

Returns the raw time format code that will be written to a stream.After reading a midi file, this method will return the timeformat that was read from the file's header. It can be changed using the setTicksPerQuarterNote() or setSmpteTimeFormat() methods.If the value returned is positive, it indicates the number of midi ticks per quarternote see setTicksPerQuarterNote().It it's negative, the upper byte indicates the framespersecond (but negative), and the lower byte is the number of ticks per frame see setSmpteTimeFormat().