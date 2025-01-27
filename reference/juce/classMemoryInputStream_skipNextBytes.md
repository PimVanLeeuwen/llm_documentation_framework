#### skipNextBytes()


 void MemoryInputStream::skipNextBytes ( int64 numBytesToSkip ) overridevirtual 
 

Reads and discards a number of bytes from the stream.Some input streams might implement this more efficiently, but the base class will just keep reading data until the requisite number of bytes have been done. For large skips it may be quicker to call setPosition() with the required position.Reimplemented from InputStream.