#### ensureSize()


 void MemoryBlock::ensureSize ( size\_t minimumSize, 
 
 bool initialiseNewSpaceToZero = false ) 

Increases the block's size only if it's smaller than a given size.Parameters

 minimumSize if the block is already bigger than this size, no action will be taken; otherwise it will be increased to this size 
 
 initialiseNewSpaceToZero if the block gets enlarged, this determines whether to clear the new section or just leave it uninitialised 



See alsosetSize