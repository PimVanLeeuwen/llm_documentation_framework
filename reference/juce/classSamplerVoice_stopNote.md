#### stopNote()


 void SamplerVoice::stopNote ( float velocity, bool allowTailOff ) overridevirtual 
 

Called to stop a note.This will be called during the rendering callback, so must be fast and threadsafe.The velocity indicates how quickly the note was released 0 is slowly, 1 is quickly.If allowTailOff is false or the voice doesn't want to tailoff, then it must stop all sound immediately, and must call clearCurrentNote() to reset the state of this voice and allow the synth to reassign it another sound.If allowTailOff is true and the voice decides to do a tailoff, then it's allowed to begin fading out its sound, and it can stop playing until it's finished. As soon as it finishes playing (during the rendering callback), it must make sure that it calls clearCurrentNote().Implements SynthesiserVoice.