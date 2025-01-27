#### createConnectionObject()


 virtual InterprocessConnection \* InterprocessConnectionServer::createConnectionObject ( ) protectedpure virtual 
 

Creates a suitable connection object for a client process that wants to connect to this one.This will be called by the listener thread when a client process tries to connect, and must return a new InterprocessConnection object that will then run as this end of the connection.See alsoInterprocessConnection