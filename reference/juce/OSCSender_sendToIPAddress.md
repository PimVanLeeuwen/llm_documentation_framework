#### sendToIPAddress() [2/2]


 bool OSCSender::sendToIPAddress ( const String & targetIPAddress, 
 
 int targetPortNumber, 
 const OSCBundle & bundle ) 

Sends an OSC bundle to a specific IP address and port.This overrides the address and port that was originally set for this sender.Parameters

 targetIPAddress The IP address to send to 
 
 targetPortNumber The target port number 
 bundle The OSC bundle to send. 



Returnstrue if the operation was successful.