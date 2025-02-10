#### writeFromInputStream()


 int64 MemoryOutputStream::writeFromInputStream ( InputStream & source, int64 maxNumBytesToWrite ) overridevirtual 
 

Reads data from an input stream and writes it to this stream.Parameters

 source the stream to read from 
 
 maxNumBytesToWrite the number of bytes to read from the stream (if this is less than zero, it will keep reading until the input is exhausted) 



Returnsthe number of bytes written Reimplemented from OutputStream.