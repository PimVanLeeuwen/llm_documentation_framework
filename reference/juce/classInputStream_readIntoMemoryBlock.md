#### readIntoMemoryBlock()


 virtual size\_t InputStream::readIntoMemoryBlock ( MemoryBlock & destBlock, ssize\_t maxNumBytesToRead = 1 ) virtual 
 

Reads from the stream and appends the data to a MemoryBlock.Parameters

 destBlock the block to append the data onto 
 
 maxNumBytesToRead if this is a positive value, it sets a limit to the number of bytes that will be read if it's negative, data will be read until the stream is exhausted. 



Returnsthe number of bytes that were added to the memory block