#### waitForNextConnection()


 StreamingSocket \* StreamingSocket::waitForNextConnection ( ) const 
 

When in "listener" mode, this waits for a connection and spawns it as a new socket.The object that gets returned will be owned by the caller.This method can only be called after using createListener().See alsocreateListener