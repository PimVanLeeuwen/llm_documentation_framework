#### findFreeVoice()


 virtual SynthesiserVoice \* Synthesiser::findFreeVoice ( SynthesiserSound \* soundToPlay, int midiChannel, int midiNoteNumber, bool stealIfNoneAvailable ) const protectedvirtual 
 

Searches through the voices to find one that's not currently playing, and which can play the given sound.Returns nullptr if all voices are busy and stealing isn't enabled.To implement a custom notestealing algorithm, you can either override this method, or (preferably) override findVoiceToSteal().