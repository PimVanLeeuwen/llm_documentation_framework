#### appliesToChannel()


 bool SamplerSound::appliesToChannel ( int midiChannel ) overridevirtual 
 

Returns true if the sound should be triggered by midi events on a given channel.The Synthesiser will use this information when deciding which sounds to trigger for a given note.Implements SynthesiserSound.