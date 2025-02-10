#### isKeyDown()


 bool SynthesiserVoice::isKeyDown ( ) const noexcept 
 

Returns true if the key that triggered this voice is still held down.Note that the voice may still be playing after the key was released (e.g because the sostenuto pedal is down).