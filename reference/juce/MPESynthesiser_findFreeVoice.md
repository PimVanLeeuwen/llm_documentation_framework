#### findFreeVoice()


 virtual MPESynthesiserVoice \* MPESynthesiser::findFreeVoice ( MPENote noteToFindVoiceFor, bool stealIfNoneAvailable ) const protectedvirtual 
 

Searches through the voices to find one that's not currently playing, and which can play the given MPE note.If all voices are active and stealIfNoneAvailable is false, this returns a nullptr. If all voices are active and stealIfNoneAvailable is true, this will call findVoiceToSteal() to find a voice.If you need to find a free voice for something else than playing a note (e.g. for deleting it), you can pass an invalid (defaultconstructed) MPENote.