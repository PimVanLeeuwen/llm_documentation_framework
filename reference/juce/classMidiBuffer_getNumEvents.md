#### getNumEvents()


 int MidiBuffer::getNumEvents ( ) const noexcept 
 

Counts the number of events in the buffer.This is actually quite a slow operation, as it has to iterate through all the events, so you might prefer to call isEmpty() if that's all you need to know.