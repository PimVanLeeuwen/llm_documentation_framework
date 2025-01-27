#### stopVoice()


 void Synthesiser::stopVoice ( SynthesiserVoice \* , float velocity, bool allowTailOff ) protected 
 

Stops a given voice.You should never need to call this, it's used internally by noteOff, but is protected in case it's useful for some custom subclasses. It basically just calls through to SynthesiserVoice::stopNote(), and has some assertions to sanitycheck a few things.