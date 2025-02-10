#### wait()


 bool WaitableEvent::wait ( double timeOutMilliseconds = 1.0 ) const 
 

Suspends the calling thread until the event has been signalled.This will wait until the object's signal() method is called by another thread, or until the timeout expires.After the event has been signalled, this method will return true and if manualReset was set to false in the WaitableEvent's constructor, then the event will be reset.Parameters

 timeOutMilliseconds the maximum time to wait, in milliseconds. A negative value will cause it to wait forever. 
 



Returnstrue if the object has been signalled, false if the timeout expires first. 
See alsosignal, reset