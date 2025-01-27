#### connectToPipe()


 bool InterprocessConnection::connectToPipe ( const String & pipeName, 
 
 int pipeReceiveMessageTimeoutMs ) 

Tries to connect the object to an existing named pipe.For this to work, another process on the same computer must already have opened an InterprocessConnection object and used createPipe() to create a pipe for this to connect to.Parameters

 pipeName the name to use for the pipe this should be unique to your app 
 
 pipeReceiveMessageTimeoutMs a timeout length to be used when reading or writing to the pipe, or 1 for an infinite timeout. 



Returnstrue if it connects successfully. 
See alsocreatePipe, NamedPipe