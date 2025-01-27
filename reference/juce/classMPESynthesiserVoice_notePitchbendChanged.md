#### notePitchbendChanged()


 virtual void MPESynthesiserVoice::notePitchbendChanged ( ) pure virtual 
 

Called by the MPESynthesiser to let the voice know that its currently playing note has changed its pitchbend value.This will be called during the rendering callback, so must be fast and threadsafe.Note: You can call currentlyPlayingNote.getFrequencyInHertz() to find out the effective frequency of the note, as a sum of the initial note number, the pernote pitchbend and the master pitchbend.