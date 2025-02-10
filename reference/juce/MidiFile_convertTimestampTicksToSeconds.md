#### convertTimestampTicksToSeconds()


 void MidiFile::convertTimestampTicksToSeconds ( ) 
 

Converts the timestamp of all the midi events from midi ticks to seconds.This will use the midi time format and tempo/time signature info in the tracks to convert all the timestamps to absolute values in seconds.