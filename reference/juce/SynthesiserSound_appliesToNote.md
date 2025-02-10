#### appliesToNote()


 virtual bool SynthesiserSound::appliesToNote ( int midiNoteNumber ) pure virtual 
 

Returns true if this sound should be played when a given midi note is pressed.The Synthesiser will use this information when deciding which sounds to trigger for a given note.Implemented in SamplerSound.