#### disconnect()


 void InterprocessConnection::disconnect ( int timeoutMs = 1, 
 
 Notify notify = Notify::yes ) 

Disconnects and closes any currentlyopen sockets or pipes.Derived classes must call this in their destructors in order to avoid undefined behaviour.Parameters

 timeoutMs the time in ms to wait before killing the thread by force 
 
 notify whether or not to call `connectionLost`