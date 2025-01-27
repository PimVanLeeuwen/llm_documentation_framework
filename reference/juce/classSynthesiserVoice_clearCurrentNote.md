#### clearCurrentNote()


 void SynthesiserVoice::clearCurrentNote ( ) protected 
 

Resets the state of this voice after a sound has finished playing.The subclass must call this when it finishes playing a note and becomes available to play new ones.It must either call it in the stopNote() method, or if the voice is tailing off, then it should call it later during the renderNextBlock method, as soon as it finishes its tailoff.It can also be called at any time during the render callback if the sound happens to have finished, e.g. if it's playing a sample and the sample finishes.