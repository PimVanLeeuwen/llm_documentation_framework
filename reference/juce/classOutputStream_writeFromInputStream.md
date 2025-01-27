#### writeFromInputStream()


 virtual int64 OutputStream::writeFromInputStream ( InputStream & source, int64 maxNumBytesToWrite ) virtual 
 

Reads data from an input stream and writes it to this stream.Parameters

 source the stream to read from 
 
 maxNumBytesToWrite the number of bytes to read from the stream (if this is less than zero, it will keep reading until the input is exhausted) 



Returnsthe number of bytes written Reimplemented in MemoryOutputStream.