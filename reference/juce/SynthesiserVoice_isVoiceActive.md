#### isVoiceActive()


 virtual bool SynthesiserVoice::isVoiceActive ( ) const virtual 
 

Returns true if this voice is currently busy playing a sound.By default this just checks the getCurrentlyPlayingNote() value, but can be overridden for more advanced checking.