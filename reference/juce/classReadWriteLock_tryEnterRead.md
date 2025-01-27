#### tryEnterRead()


 bool ReadWriteLock::tryEnterRead ( ) const noexcept 
 

Tries to lock this object for reading.Multiple threads can simultaneously lock the object for reading, but if another thread has it locked for writing, then this will fail and return false.Returnstrue if the lock is successfully gained. 
See alsoexitRead, ScopedTryReadLock