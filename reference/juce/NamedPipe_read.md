#### read()


 int NamedPipe::read ( void \* destBuffer, 
 
 int maxBytesToRead, 
 int timeOutMilliseconds ) 

Reads data from the pipe.This will block until another thread has written enough data into the pipe to fill the number of bytes specified, or until another thread calls the cancelPendingReads() method.If the operation fails, it returns 1, otherwise, it will return the number of bytes read.If timeOutMilliseconds is less than zero, it will wait indefinitely, otherwise this is a maximum timeout for reading from the pipe.