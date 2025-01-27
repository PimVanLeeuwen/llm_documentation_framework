#### copyTo()


 void MemoryBlock::copyTo ( void \* destData, int sourceOffset, size\_t numBytes ) const noexcept 
 

Copies data from this MemoryBlock to a memory address.Parameters

 destData the memory location to write to 
 
 sourceOffset the offset within this block from which the copied data will be read 
 numBytes how much to copy (if this extends beyond the limits of the memory block, zeros will be used for that portion of the data)