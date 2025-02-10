#### noteKeyStateChanged()


 virtual void MPESynthesiserVoice::noteKeyStateChanged ( ) pure virtual 
 

Called by the MPESynthesiser to let the voice know that its currently playing note has changed its key state.This typically happens when a sustain or sostenuto pedal is pressed or released (on an MPE channel relevant for this note), or if the note key is lifted while the sustained or sostenuto pedal is still held down. This will be called during the rendering callback, so must be fast and threadsafe.