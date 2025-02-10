#### read()


 int StreamingSocket::read ( void \* destBuffer, 
 
 int maxBytesToRead, 
 bool blockUntilSpecifiedAmountHasArrived ) 

Reads bytes from the socket.If blockUntilSpecifiedAmountHasArrived is true, the method will block until maxBytesToRead bytes have been read, (or until an error occurs). If this flag is false, the method will return as much data as is currently available without blocking.Returnsthe number of bytes read, or 1 if there was an error 
See alsowaitUntilReady