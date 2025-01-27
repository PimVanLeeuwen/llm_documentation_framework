#### write()


 int DatagramSocket::write ( const String & remoteHostname, 
 
 int remotePortNumber, 
 const void \* sourceBuffer, 
 int numBytesToWrite ) 

Writes bytes to the socket from a buffer.Note that this method will block unless you have checked the socket is ready for writing before calling it (see the waitUntilReady() method).Returnsthe number of bytes written, or 1 if there was an error