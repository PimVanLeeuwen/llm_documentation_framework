#### isActive()


 virtual bool MPESynthesiserVoice::isActive ( ) const virtual 
 

Returns true if this voice is currently busy playing a sound.By default this just checks whether getCurrentlyPlayingNote() returns a valid MPE note, but can be overridden for more advanced checking.