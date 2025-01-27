#### createPipe()


 bool InterprocessConnection::createPipe ( const String & pipeName, 
 
 int pipeReceiveMessageTimeoutMs, 
 bool mustNotExist = false ) 

Tries to create a new pipe for other processes to connect to.This creates a pipe with the given name, so that other processes can use connectToPipe() to connect to the other end.Parameters

 pipeName the name to use for the pipe this should be unique to your app 
 
 pipeReceiveMessageTimeoutMs a timeout length to be used when reading or writing to the pipe, or 1 for an infinite timeout 
 mustNotExist if set to true, the method will fail if the pipe already exists 



Returnstrue if the pipe was created, or false if it fails (e.g. if another process is already using the pipe)