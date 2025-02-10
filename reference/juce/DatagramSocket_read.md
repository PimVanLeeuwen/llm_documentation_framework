#### read() [2/2]


 int DatagramSocket::read ( void \* destBuffer, 
 
 int maxBytesToRead, 
 bool blockUntilSpecifiedAmountHasArrived, 
 String & senderIPAddress, 
 int & senderPortNumber ) 

Reads bytes from the socket and return the IP address of the sender.If blockUntilSpecifiedAmountHasArrived is true, the method will block until maxBytesToRead bytes have been read, (or until an error occurs). If this flag is false, the method will return as much data as is currently available without blocking.Returnsthe number of bytes read, or 1 if there was an error. On a successful result, the senderIPAddress value will be set to the IP of the sender 
See alsowaitUntilReady