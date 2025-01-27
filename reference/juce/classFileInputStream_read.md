#### read()


 int FileInputStream::read ( void \* destBuffer, int maxBytesToRead ) overridevirtual 
 

Reads some data from the stream into a memory buffer.This is the only read method that subclasses actually need to implement, as the InputStream base class implements the other read methods in terms of this one (although it's often more efficient for subclasses to implement them directly).Parameters

 destBuffer the destination buffer for the data. This must not be null. 
 
 maxBytesToRead the maximum number of bytes to read make sure the memory block passed in is big enough to contain this many bytes. This value must not be negative. 



Returnsthe actual number of bytes that were read, which may be less than maxBytesToRead if the stream is exhausted before it gets that far Implements InputStream.