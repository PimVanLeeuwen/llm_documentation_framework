#### createListener()


 bool StreamingSocket::createListener ( int portNumber, 
 
 const String & localHostName = String() ) 

Puts this socket into "listener" mode.When in this mode, your thread can call waitForNextConnection() repeatedly, which will spawn new sockets for each new connection, so that these can be handled in parallel by other threads.Parameters

 portNumber the port number to listen on 
 
 localHostName the interface address to listen on pass an empty string to listen on all addresses 



Returnstrue if it manages to open the socket successfully 
See alsowaitForNextConnection