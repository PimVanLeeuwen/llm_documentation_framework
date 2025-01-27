#### ensureSize()


 void MidiBuffer::ensureSize ( size\_t minimumNumBytes ) 
 

Preallocates some memory for the buffer to use.This helps to avoid needing to reallocate space when the buffer has messages added to it.