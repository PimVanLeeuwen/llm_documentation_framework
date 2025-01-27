#### addSound()


 SynthesiserSound \* Synthesiser::addSound ( const SynthesiserSound::Ptr & newSound ) 
 

Adds a new sound to the synthesiser.The object passed in is reference counted, so will be deleted when the synthesiser and all voices are no longer using it.