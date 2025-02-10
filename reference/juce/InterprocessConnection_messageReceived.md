#### messageReceived()


 virtual void InterprocessConnection::messageReceived ( const MemoryBlock & message ) pure virtual 
 

Called when a message arrives.When the object at the other end of this connection sends us a message with sendMessage(), this callback is used to deliver it to us.If the connection was created with the callbacksOnMessageThread flag set, then this will be called on the message thread; otherwise it will be called on a server thread.See alsosendMessage