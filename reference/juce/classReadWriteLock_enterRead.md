#### enterRead()


 void ReadWriteLock::enterRead ( ) const noexcept 
 

Locks this object for reading.Multiple threads can simultaneously lock the object for reading, but if another thread has it locked for writing, then this will block until it releases the lock.See alsoexitRead, ScopedReadLock