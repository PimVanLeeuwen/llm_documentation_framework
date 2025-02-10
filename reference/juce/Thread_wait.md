#### wait()


 bool Thread::wait ( double timeOutMilliseconds ) const 
 

Suspends the execution of this thread until either the specified timeout period has elapsed, or another thread calls the notify() method to wake it up.A negative timeout value means that the method will wait indefinitely.Returnstrue if the event has been signalled, false if the timeout expires.