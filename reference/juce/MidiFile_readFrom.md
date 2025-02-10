#### readFrom()


 bool MidiFile::readFrom ( InputStream & sourceStream, 
 
 bool createMatchingNoteOffs = true, 
 int \* midiFileType = nullptr ) 

Reads a midi file format stream.After calling this, you can get the tracks that were read from the file by using the getNumTracks() and getTrack() methods.The timestamps of the midi events in the tracks will represent their positions in terms of midi ticks. To convert them to seconds, use the convertTimestampTicksToSeconds() method.Parameters

 sourceStream the source stream 
 
 createMatchingNoteOffs if true, any missing noteoffs for previous noteons will be automatically added at the end of the file by calling MidiMessageSequence::updateMatchedPairs on each track. 
 midiFileType if not nullptr, the integer at this address will be set to 0, 1, or 2 depending on the type of the midi file 



Returnstrue if the stream was read successfully