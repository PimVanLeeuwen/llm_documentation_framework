#### flush()


 void MemoryOutputStream::flush ( ) overridevirtual 
 

If the stream is writing to a usersupplied MemoryBlock, this will trim any excess capacity off the block, so that its length matches the amount of actual data that has been written so far.Implements OutputStream.