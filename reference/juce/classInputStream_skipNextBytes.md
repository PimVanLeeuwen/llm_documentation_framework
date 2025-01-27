#### skipNextBytes()


 virtual void InputStream::skipNextBytes ( int64 numBytesToSkip ) virtual 
 

Reads and discards a number of bytes from the stream.Some input streams might implement this more efficiently, but the base class will just keep reading data until the requisite number of bytes have been done. For large skips it may be quicker to call setPosition() with the required position.Reimplemented in MemoryInputStream.