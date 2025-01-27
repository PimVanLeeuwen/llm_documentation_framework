#### write()


 bool MemoryOutputStream::write ( const void \* dataToWrite, size\_t numberOfBytes ) overridevirtual 
 

Writes a block of data to the stream.When creating a subclass of OutputStream, this is the only write method that needs to be overloaded the base class has methods for writing other types of data which use this to do the work.Parameters

 dataToWrite the target buffer to receive the data. This must not be null. 
 
 numberOfBytes the number of bytes to write. 



Returnsfalse if the write operation fails for some reason Implements OutputStream.