#### enter()


 void SpinLock::enter ( ) const noexcept 
 

Acquires the lock.This will block until the lock has been successfully acquired by this thread. Note that a SpinLock is NOT reentrant, and is not smart enough to know whether the caller thread already has the lock so if a thread tries to acquire a lock that it already holds, this method will never return!It's strongly recommended that you never call this method directly instead use the ScopedLockType class to manage the locking using an RAII pattern instead.