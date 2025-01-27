#### startNote()


 void SamplerVoice::startNote ( int midiNoteNumber, float velocity, SynthesiserSound \* sound, int currentPitchWheelPosition ) overridevirtual 
 

Called to start a new note.This will be called during the rendering callback, so must be fast and threadsafe.Implements SynthesiserVoice.