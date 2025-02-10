#### reduceNumVoices()


 void MPESynthesiser::reduceNumVoices ( int newNumVoices ) 
 

Reduces the number of voices to newNumVoices.This will repeatedly call findVoiceToSteal() and remove that voice, until the total number of voices equals newNumVoices. If newNumVoices is greater than or equal to the current number of voices, this method does nothing.