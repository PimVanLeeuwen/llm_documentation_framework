#### setNoteStealingEnabled()


 void Synthesiser::setNoteStealingEnabled ( bool shouldStealNotes ) 
 

If set to true, then the synth will try to take over an existing voice if it runs out and needs to play another note.The value of this boolean is passed into findFreeVoice(), so the result will depend on the implementation of this method.