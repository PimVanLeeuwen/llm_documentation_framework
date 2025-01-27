#### noteStarted()


 virtual void MPESynthesiserVoice::noteStarted ( ) pure virtual 
 

Called by the MPESynthesiser to let the voice know that a new note has started on it.This will be called during the rendering callback, so must be fast and threadsafe.