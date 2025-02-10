#### getBoundPort()


 int StreamingSocket::getBoundPort ( ) const noexcept 
 

Returns the local port number to which this socket is currently bound.This is useful if you need to know to which port the OS has actually bound your socket when calling the constructor or bindToPort with zero as the localPortNumber argument.Returns1 if the function fails