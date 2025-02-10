#### noteTimbreChanged()


 virtual void MPESynthesiserVoice::noteTimbreChanged ( ) pure virtual 
 

Called by the MPESynthesiser to let the voice know that its currently playing note has changed its timbre value.This will be called during the rendering callback, so must be fast and threadsafe.