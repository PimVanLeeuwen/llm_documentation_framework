#### getNextIndexAtTime()


 int MidiMessageSequence::getNextIndexAtTime ( double timeStamp ) const noexcept 
 

Returns the index of the first event on or after the given timestamp.If the time is beyond the end of the sequence, this will return the number of events.