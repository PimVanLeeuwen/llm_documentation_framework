#### connectToSocket()


 bool OSCSender::connectToSocket ( DatagramSocket & socket, 
 
 const String & targetHostName, 
 int targetPortNumber ) 

Uses an existing datagram socket for sending OSC packets to the specified target.Parameters

 socket An existing datagram socket. Make sure this doesn't get deleted while this class is still using it! 
 
 targetHostName The remote host to which messages will be send. 
 targetPortNumber The remote UDP port number on which the host will receive the messages. 



Returnstrue if the connection was successful; false otherwise. 
See alsoconnect, send, disconnect.