#### connectToSocket()


 bool InterprocessConnection::connectToSocket ( const String & hostName, 
 
 int portNumber, 
 int timeOutMillisecs ) 

Tries to connect this object to a socket.For this to work, the machine on the other end needs to have a InterprocessConnectionServer object waiting to receive client connections on this port number.Parameters

 hostName the host computer, either a network address or name 
 
 portNumber the socket port number to try to connect to 
 timeOutMillisecs how long to keep trying before giving up 



Returnstrue if the connection is established successfully 
See alsoSocket