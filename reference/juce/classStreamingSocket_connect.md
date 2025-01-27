#### connect()


 bool StreamingSocket::connect ( const String & remoteHostname, 
 
 int remotePortNumber, 
 int timeOutMillisecs = 3000 ) 

Tries to connect the socket to hostname:port.If timeOutMillisecs is 0, then this method will block until the operating system rejects the connection (which could take a long time).Returnstrue if it succeeds, false if otherwise 
See alsoisConnected