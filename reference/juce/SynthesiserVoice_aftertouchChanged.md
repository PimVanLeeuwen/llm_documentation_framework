#### aftertouchChanged()


 virtual void SynthesiserVoice::aftertouchChanged ( int newAftertouchValue ) virtual 
 

Called to let the voice know that the aftertouch has changed.This will be called during the rendering callback, so must be fast and threadsafe.