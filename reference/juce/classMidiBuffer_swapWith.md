#### swapWith()


 void MidiBuffer::swapWith ( MidiBuffer & ) noexcept 
 

Exchanges the contents of this buffer with another one.This is a quick operation, because no memory allocating or copying is done, it just swaps the internal state of the two buffers.