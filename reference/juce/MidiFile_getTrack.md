#### getTrack()


 const MidiMessageSequence \* MidiFile::getTrack ( int index ) const noexcept 
 

Returns a pointer to one of the tracks in the file.Returnsa pointer to the track, or nullptr if the index is outofrange 
See alsogetNumTracks, addTrack