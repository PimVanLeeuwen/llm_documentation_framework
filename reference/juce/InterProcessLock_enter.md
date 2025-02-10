#### enter()


 bool InterProcessLock::enter ( int timeOutMillisecs = 1 ) 
 

Attempts to lock the critical section.Parameters

 timeOutMillisecs how many milliseconds to wait if the lock is already held by another process a value of 0 will return immediately, negative values will wait forever 
 



Returnstrue if the lock could be gained within the timeout period, or false if the timeout expired. Referenced by InterProcessLock::ScopedLockType::ScopedLockType().