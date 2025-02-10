#### prepareToWrite()


 void AbstractFifo::prepareToWrite ( int numToWrite, int & startIndex1, int & blockSize1, int & startIndex2, int & blockSize2 ) const noexcept 
 

Returns the location within the buffer at which an incoming block of data should be written.Because the section of data that you want to add to the buffer may overlap the end and wrap around to the start, two blocks within your buffer are returned, and you should copy your data into the first one, with any remaining data spilling over into the second.If the number of items you ask for is too large to fit within the buffer's free space, then blockSize1 + blockSize2 may add up to a lower value than numToWrite. If this happens, you may decide to keep waiting and retrying the method until there's enough space available.After calling this method, if you choose to write your data into the blocks returned, you must call finishedWrite() to tell the FIFO how much data you actually added.e.g.void addToFifo (const int\* someData, int numItems)
{
 int start1, size1, start2, size2;
 prepareToWrite (numItems, start1, size1, start2, size2);
 
 if (size1 > 0)
 copySomeData (myBuffer + start1, someData, size1);
 
 if (size2 > 0)
 copySomeData (myBuffer + start2, someData + size1, size2);
 
 finishedWrite (size1 + size2);
}
AbstractFifo::finishedWritevoid finishedWrite(int numWritten) noexceptCalled after writing from the FIFO, to indicate that this many items have been added.
AbstractFifo::prepareToWritevoid prepareToWrite(int numToWrite, int &startIndex1, int &blockSize1, int &startIndex2, int &blockSize2) const noexceptReturns the location within the buffer at which an incoming block of data should be written.
Parameters

 numToWrite indicates how many items you'd like to add to the buffer 
 
 startIndex1 on exit, this will contain the start index in your buffer at which your data should be written 
 blockSize1 on exit, this indicates how many items can be written to the block starting at startIndex1 
 startIndex2 on exit, this will contain the start index in your buffer at which any data that didn't fit into the first block should be written 
 blockSize2 on exit, this indicates how many items can be written to the block starting at startIndex2 



See alsofinishedWrite