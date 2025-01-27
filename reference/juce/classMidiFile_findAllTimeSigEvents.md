#### findAllTimeSigEvents()


 void MidiFile::findAllTimeSigEvents ( MidiMessageSequence & timeSigEvents ) const 
 

Makes a list of all the timesignature metaevents from all tracks in the midi file.Useful for finding the positions of all the tempo changes in a file.Parameters

 timeSigEvents a list to which all the events will be added