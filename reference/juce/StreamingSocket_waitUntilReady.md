#### waitUntilReady()


 int StreamingSocket::waitUntilReady ( bool readyForReading, 
 
 int timeoutMsecs ) 

Waits until the socket is ready for reading or writing.If readyForReading is true, it will wait until the socket is ready for reading; if false, it will wait until it's ready for writing.If the timeout is < 0, it will wait forever, or else will give up after the specified time.Returns1 if the socket is ready on return, 0 if it timesout before the socket becomes ready, or 1 if an error occurs