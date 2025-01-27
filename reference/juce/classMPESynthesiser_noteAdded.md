#### noteAdded()


 void MPESynthesiser::noteAdded ( MPENote newNote ) overrideprotectedvirtual 
 

Attempts to start playing a new note.The default method here will find a free voice that is appropriate for playing the given MPENote, and use that voice to start playing the sound. If isNoteStealingEnabled returns true (set this by calling setNoteStealingEnabled), the synthesiser will use the voice stealing algorithm to find a free voice for the note (if no voices are free otherwise).This method will be called automatically according to the midi data passed into renderNextBlock(). Do not call it yourself, otherwise the internal MPE note state will become inconsistent.Reimplemented from MPEInstrument::Listener.