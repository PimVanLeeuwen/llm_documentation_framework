#### getBoundPort()


 int DatagramSocket::getBoundPort ( ) const noexcept 
 

Returns the local port number to which this socket is currently bound.This is useful if you need to know to which port the OS has actually bound your socket when bindToPort was called with zero.Returns1 if the socket didn't bind to any port yet or an error occurred