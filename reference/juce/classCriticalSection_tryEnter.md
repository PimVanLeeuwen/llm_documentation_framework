#### tryEnter()


 bool CriticalSection::tryEnter ( ) const noexcept 
 

Attempts to lock this critical section without blocking.This method behaves identically to CriticalSection::enter, except that the caller thread does not wait if the lock is currently held by another thread but returns false immediately.Returnsfalse if the lock is currently held by another thread, true otherwise. 
See alsoenter