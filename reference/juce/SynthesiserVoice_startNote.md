#### startNote()


 virtual void SynthesiserVoice::startNote ( int midiNoteNumber, float velocity, SynthesiserSound \* sound, int currentPitchWheelPosition ) pure virtual 
 

Called to start a new note.This will be called during the rendering callback, so must be fast and threadsafe.Implemented in SamplerVoice.