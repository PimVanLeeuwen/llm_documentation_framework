#### sendMessage()


 bool InterprocessConnection::sendMessage ( const MemoryBlock & message ) 
 

Tries to send a message to the other end of this connection.This will fail if it's not connected, or if there's some kind of write error. If it succeeds, the connection object at the other end will receive the message by a callback to its messageReceived() method.See alsomessageReceived