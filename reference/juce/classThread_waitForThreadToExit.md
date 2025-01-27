#### waitForThreadToExit()


 bool Thread::waitForThreadToExit ( int timeOutMilliseconds ) const 
 

Waits for the thread to stop.This will wait until isThreadRunning() is false or until a timeout expires.Parameters

 timeOutMilliseconds the time to wait, in milliseconds. If this value is less than zero, it will wait forever. 
 



Returnstrue if the thread exits, or false if the timeout expires first.