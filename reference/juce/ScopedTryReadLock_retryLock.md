#### retryLock()


 bool ScopedTryReadLock::retryLock ( ) noexcept 
 

Retry gaining the lock by calling tryEnter on the underlying lock.