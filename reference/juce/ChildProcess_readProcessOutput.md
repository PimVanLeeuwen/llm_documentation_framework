#### readProcessOutput()


 int ChildProcess::readProcessOutput ( void \* destBuffer, 
 
 int numBytesToRead ) 

Attempts to read some output from the child process.This will attempt to read up to the given number of bytes of data from the process. It returns the number of bytes that were actually read.