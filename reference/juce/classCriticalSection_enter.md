#### enter()


 void CriticalSection::enter ( ) const noexcept 
 

Acquires the lock.If the lock is already held by the caller thread, the method returns immediately. If the lock is currently held by another thread, this will wait until it becomes free.It's strongly recommended that you never call this method directly instead use the ScopedLock class to manage the locking using an RAII pattern instead.See alsoexit, tryEnter, ScopedLock