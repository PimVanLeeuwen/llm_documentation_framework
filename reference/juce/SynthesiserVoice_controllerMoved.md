#### controllerMoved()


 virtual void SynthesiserVoice::controllerMoved ( int controllerNumber, int newControllerValue ) pure virtual 
 

Called to let the voice know that a midi controller has been moved.This will be called during the rendering callback, so must be fast and threadsafe.Implemented in SamplerVoice.