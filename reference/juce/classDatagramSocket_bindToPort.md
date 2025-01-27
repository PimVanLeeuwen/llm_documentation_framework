#### bindToPort() [2/2]


 bool DatagramSocket::bindToPort ( int localPortNumber, 
 
 const String & localAddress ) 

Binds the socket to the specified local port and local address.If localAddress is not an empty string then the socket will be bound to localAddress as well. This is useful if you would like to bind your socket to a specific network adapter. Note that localAddress must be an IP address assigned to one of your network address otherwise this function will fail.Returnstrue on success; false may indicate that another socket is already bound on the same port 
See alsobindToPort (int localPortNumber), IPAddress::getAllAddresses