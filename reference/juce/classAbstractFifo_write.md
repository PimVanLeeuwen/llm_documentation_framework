#### write()


 ScopedWrite AbstractFifo::write ( int numToWrite ) noexcept 
 

Replaces prepareToWrite/finishedWrite with a single function.This function returns an object which contains the start indices and block sizes, and also automatically finishes the write operation when it goes out of scope.{
 auto writeHandle = fifo.write (5);
 
 for (auto i = 0; i != writeHandle.blockSize1; ++i)
 {
 // write the item at index writeHandle.startIndex1 + i
 }
 
 for (auto i = 0; i != writeHandle.blockSize2; ++i)
 {
 // write the item at index writeHandle.startIndex2 + i
 }
} // writeHandle goes out of scope here, finishing the write operation