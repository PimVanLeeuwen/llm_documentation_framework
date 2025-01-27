#### clear() [2/2]


 void MidiBuffer::clear ( int start, 
 
 int numSamples ) 

Removes all events between two times from the buffer.All events for which (start <= event position < start + numSamples) will be removed.