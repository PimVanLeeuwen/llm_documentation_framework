#### findVoiceToSteal()


 virtual MPESynthesiserVoice \* MPESynthesiser::findVoiceToSteal ( MPENote noteToStealVoiceFor = MPENote() ) const protectedvirtual 
 

Chooses a voice that is most suitable for being reused to play a new note, or for being deleted by reduceNumVoices.The default method will attempt to find the oldest voice that isn't the bottom or top note being played. If that's not suitable for your synth, you can override this method and do something more cunning instead.If you pass a valid MPENote for the optional argument, then the note number of that note will be taken into account for finding the ideal voice to steal. If you pass an invalid (defaultconstructed) MPENote instead, this part of the algorithm will be ignored.