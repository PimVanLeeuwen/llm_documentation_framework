#### prepareToRead()


 void AbstractFifo::prepareToRead ( int numWanted, int & startIndex1, int & blockSize1, int & startIndex2, int & blockSize2 ) const noexcept 
 

Returns the location within the buffer from which the next block of data should be read.Because the section of data that you want to read from the buffer may overlap the end and wrap around to the start, two blocks within your buffer are returned, and you should read from both of them.If the number of items you ask for is greater than the amount of data available, then blockSize1 + blockSize2 may add up to a lower value than numWanted. If this happens, you may decide to keep waiting and retrying the method until there's enough data available.After calling this method, if you choose to read the data, you must call finishedRead() to tell the FIFO how much data you have consumed.e.g.void readFromFifo (int\* someData, int numItems)
{
 int start1, size1, start2, size2;
 prepareToRead (numSamples, start1, size1, start2, size2);
 
 if (size1 > 0)
 copySomeData (someData, myBuffer + start1, size1);
 
 if (size2 > 0)
 copySomeData (someData + size1, myBuffer + start2, size2);
 
 finishedRead (size1 + size2);
}
AbstractFifo::finishedReadvoid finishedRead(int numRead) noexceptCalled after reading from the FIFO, to indicate that this many items have now been consumed.
AbstractFifo::prepareToReadvoid prepareToRead(int numWanted, int &startIndex1, int &blockSize1, int &startIndex2, int &blockSize2) const noexceptReturns the location within the buffer from which the next block of data should be read.
Parameters

 numWanted indicates how many items you'd like to read from the buffer 
 
 startIndex1 on exit, this will contain the start index in your buffer at which your data should be written 
 blockSize1 on exit, this indicates how many items can be written to the block starting at startIndex1 
 startIndex2 on exit, this will contain the start index in your buffer at which any data that didn't fit into the first block should be written 
 blockSize2 on exit, this indicates how many items can be written to the block starting at startIndex2 



See alsofinishedRead