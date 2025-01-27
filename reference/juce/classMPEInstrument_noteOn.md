#### noteOn()


 virtual void MPEInstrument::noteOn ( int midiChannel, int midiNoteNumber, MPEValue midiNoteOnVelocity ) virtual 
 

Request a noteon on the given channel, with the given initial note number and velocity.If the message arrives on a valid note channel, this will create a new MPENote and call the noteAdded callback.