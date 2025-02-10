#### insert()


 void MemoryBlock::insert ( const void \* dataToInsert, 
 
 size\_t numBytesToInsert, 
 size\_t insertPosition ) 

Inserts some data into the block.The dataToInsert pointer must not be null. This block's size will be increased accordingly. If the insert position lies outside the valid range of the block, it will be clipped to within the range before being used.