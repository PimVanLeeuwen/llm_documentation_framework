#### read()


 int WebInputStream::read ( void \* destBuffer, int maxBytesToRead ) overridevirtual 
 

Reads some data from the stream into a memory buffer.This method will block until the maxBytesToRead bytes are available.This method calls connect() internally if the connection hasn't already been established.Parameters

 destBuffer the destination buffer for the data. This must not be null. 
 
 maxBytesToRead the maximum number of bytes to read make sure the memory block passed in is big enough to contain this many bytes. This value must not be negative. 



Returnsthe actual number of bytes that were read, which may be less than maxBytesToRead if the stream is exhausted before it gets that far Implements InputStream.