#### sustainPedal()


 virtual void MPEInstrument::sustainPedal ( int midiChannel, bool isDown ) virtual 
 

Request a sustain pedal press or release.If midiChannel is a zone's master channel, this will act on all notes in that zone; otherwise, nothing will happen.