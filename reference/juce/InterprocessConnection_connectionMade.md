#### connectionMade()


 virtual void InterprocessConnection::connectionMade ( ) pure virtual 
 

Called when the connection is first connected.If the connection was created with the callbacksOnMessageThread flag set, then this will be called on the message thread; otherwise it will be called on a server thread.