#### pitchWheelMoved()


 virtual void SynthesiserVoice::pitchWheelMoved ( int newPitchWheelValue ) pure virtual 
 

Called to let the voice know that the pitch wheel has been moved.This will be called during the rendering callback, so must be fast and threadsafe.Implemented in SamplerVoice.