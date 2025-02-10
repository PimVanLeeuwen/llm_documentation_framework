#### turnOffAllVoices()


 virtual void MPESynthesiser::turnOffAllVoices ( bool allowTailOff ) virtual 
 

Release all MPE notes and turn off all voices.If allowTailOff is true, the voices will be allowed to fade out the notes gracefully (if they can do). If this is false, the notes will all be cut off immediately.This method is meant to be called by the user, for example to implement a MIDI panic button in a synth.