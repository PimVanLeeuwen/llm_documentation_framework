#### addVoice()


 void MPESynthesiser::addVoice ( MPESynthesiserVoice \* newVoice ) 
 

Adds a new voice to the synth.All the voices should be the same class of object and are treated equally.The object passed in will be managed by the synthesiser, which will delete it later on when no longer needed. The caller should not retain a pointer to the voice.