#### removeSection()


 void MemoryBlock::removeSection ( size\_t startByte, 
 
 size\_t numBytesToRemove ) 

Chops out a section of the block.This will remove a section of the memory block and close the gap around it, shifting any subsequent data downwards and reducing the size of the block.If the range specified goes beyond the size of the block, it will be clipped.