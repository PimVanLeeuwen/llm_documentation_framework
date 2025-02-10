#### beginWaitingForSocket()


 bool InterprocessConnectionServer::beginWaitingForSocket ( int portNumber, 
 
 const String & bindAddress = String() ) 

Starts an internal thread which listens on the given port number.While this is running, if another process tries to connect with the InterprocessConnection::connectToSocket() method, this object will call createConnectionObject() to create a connection to that client.Use stop() to stop the thread running.Parameters

 portNumber The port on which the server will receive connections 
 
 bindAddress The address on which the server will listen for connections. An empty string indicates that it should listen on all addresses assigned to this machine. 



See alsocreateConnectionObject, stop