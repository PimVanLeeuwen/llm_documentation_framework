#### getBoundPort()


 int InterprocessConnectionServer::getBoundPort ( ) const noexcept 
 

Returns the local port number to which this server is currently bound.This is useful if you need to know to which port the OS has actually bound your socket when calling beginWaitingForSocket with a port number of zero.Returns 1 if the function fails.