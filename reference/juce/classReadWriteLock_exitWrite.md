#### exitWrite()


 void ReadWriteLock::exitWrite ( ) const noexcept 
 

Releases the writelock.If the caller thread hasn't got the lock, this can have unpredictable results.If the enterWrite() method has been called multiple times by the thread, each call must be matched by a call to exit() before other threads will be allowed to take over the lock.See alsoenterWrite, ScopedWriteLock