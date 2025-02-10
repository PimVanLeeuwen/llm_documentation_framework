#### setSize()


 void MemoryBlock::setSize ( size\_t newSize, 
 
 bool initialiseNewSpaceToZero = false ) 

Resizes the memory block.Any data that is present in both the old and new sizes will be retained. When enlarging the block, the new space that is allocated at the end can either be cleared, or left uninitialised.Parameters

 newSize the new desired size for the block 
 
 initialiseNewSpaceToZero if the block gets enlarged, this determines whether to clear the new section or just leave it uninitialised 



See alsoensureSize