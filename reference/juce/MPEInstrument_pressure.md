#### pressure()


 virtual void MPEInstrument::pressure ( int midiChannel, MPEValue value ) virtual 
 

Request a pressure change on the given channel with the given value.This will modify the pressure dimension of the note currently held down on this channel (if any). If the channel is a zone master channel, the pressure change will be broadcast to all notes in this zone.