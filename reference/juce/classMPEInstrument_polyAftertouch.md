#### polyAftertouch()


 virtual void MPEInstrument::polyAftertouch ( int midiChannel, int midiNoteNumber, MPEValue value ) virtual 
 

Request a polyaftertouch change for a given note number.The change will be broadcast to all notes sharing the channel and note number of the change message.