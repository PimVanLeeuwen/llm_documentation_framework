#### copyFrom()


 void MemoryBlock::copyFrom ( const void \* srcData, int destinationOffset, size\_t numBytes ) noexcept 
 

Copies data into this MemoryBlock from a memory address.Parameters

 srcData the memory location of the data to copy into this block 
 
 destinationOffset the offset in this block at which the data being copied should begin 
 numBytes how much to copy in (if this goes beyond the size of the memory block, it will be clipped so not to do anything nasty)