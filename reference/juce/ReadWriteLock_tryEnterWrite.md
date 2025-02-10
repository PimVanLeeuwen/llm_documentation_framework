#### tryEnterWrite()


 bool ReadWriteLock::tryEnterWrite ( ) const noexcept 
 

Tries to lock this object for writing.This is like enterWrite(), but doesn't block it returns true if it manages to obtain the lock.Returnstrue if the lock is successfully gained. 
See alsoenterWrite, ScopedTryWriteLock