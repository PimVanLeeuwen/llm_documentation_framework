#### sostenutoPedal()


 virtual void MPEInstrument::sostenutoPedal ( int midiChannel, bool isDown ) virtual 
 

Request a sostenuto pedal press or release.If midiChannel is a zone's master channel, this will act on all notes in that zone; otherwise, nothing will happen.