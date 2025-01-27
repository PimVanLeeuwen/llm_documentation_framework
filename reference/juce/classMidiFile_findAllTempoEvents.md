#### findAllTempoEvents()


 void MidiFile::findAllTempoEvents ( MidiMessageSequence & tempoChangeEvents ) const 
 

Makes a list of all the tempochange metaevents from all tracks in the midi file.Useful for finding the positions of all the tempo changes in a file.Parameters

 tempoChangeEvents a list to which all the events will be added