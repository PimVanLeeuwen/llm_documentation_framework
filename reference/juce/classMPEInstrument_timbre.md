#### timbre()


 virtual void MPEInstrument::timbre ( int midiChannel, MPEValue value ) virtual 
 

Request a third dimension (timbre) change on the given channel with the given value.This will modify the timbre dimension of the note currently held down on this channel (if any). If the channel is a zone master channel, the timbre change will be broadcast to all notes in this zone.