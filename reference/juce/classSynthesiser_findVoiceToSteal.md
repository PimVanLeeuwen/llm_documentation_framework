#### findVoiceToSteal()


 virtual SynthesiserVoice \* Synthesiser::findVoiceToSteal ( SynthesiserSound \* soundToPlay, int midiChannel, int midiNoteNumber ) const protectedvirtual 
 

Chooses a voice that is most suitable for being reused.The default method will attempt to find the oldest voice that isn't the bottom or top note being played. If that's not suitable for your synth, you can override this method and do something more cunning instead.