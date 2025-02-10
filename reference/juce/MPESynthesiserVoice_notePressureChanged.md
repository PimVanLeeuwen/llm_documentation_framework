#### notePressureChanged()


 virtual void MPESynthesiserVoice::notePressureChanged ( ) pure virtual 
 

Called by the MPESynthesiser to let the voice know that its currently playing note has changed its pressure value.This will be called during the rendering callback, so must be fast and threadsafe.