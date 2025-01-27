#### connectToSocket()


 bool OSCReceiver::connectToSocket ( DatagramSocket & socketToUse ) 
 

Connects to a UDP datagram socket that is already set up, and starts listening to OSC packets arriving on this port.Make sure that the object you give it doesn't get deleted while this object is still using it!Returnstrue if the connection was successful; false otherwise.