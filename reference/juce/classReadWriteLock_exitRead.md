#### exitRead()


 void ReadWriteLock::exitRead ( ) const noexcept 
 

Releases the readlock.If the caller thread hasn't got the lock, this can have unpredictable results.If the enterRead() method has been called multiple times by the thread, each call must be matched by a call to exitRead() before other threads will be allowed to take over the lock.See alsoenterRead, ScopedReadLock