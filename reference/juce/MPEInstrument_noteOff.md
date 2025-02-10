#### noteOff()


 virtual void MPEInstrument::noteOff ( int midiChannel, int midiNoteNumber, MPEValue midiNoteOffVelocity ) virtual 
 

Request a noteoff.If there is a matching playing note, this will release the note (except if it is sustained by a sustain or sostenuto pedal) and call the noteReleased callback.