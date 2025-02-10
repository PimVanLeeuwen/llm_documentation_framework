#### read()


 ScopedRead AbstractFifo::read ( int numToRead ) noexcept 
 

Replaces prepareToRead/finishedRead with a single function.This function returns an object which contains the start indices and block sizes, and also automatically finishes the read operation when it goes out of scope.{
 auto readHandle = fifo.read (4);
 
 for (auto i = 0; i != readHandle.blockSize1; ++i)
 {
 // read the item at index readHandle.startIndex1 + i
 }
 
 for (auto i = 0; i != readHandle.blockSize2; ++i)
 {
 // read the item at index readHandle.startIndex2 + i
 }
} // readHandle goes out of scope here, finishing the read operation