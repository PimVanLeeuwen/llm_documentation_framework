#### connect()


 bool OSCSender::connect ( const String & targetHostName, 
 
 int targetPortNumber ) 

Connects to a datagram socket and prepares the socket for sending OSC packets to the specified target.Note: The operating system will choose which specific network adapter(s) to bind your socket to, and which local port to use for the sender.Parameters

 targetHostName The remote host to which messages will be send. 
 
 targetPortNumber The remote UDP port number on which the host will receive the messages. 



Returnstrue if the connection was successful; false otherwise. 
See alsosend, disconnect.