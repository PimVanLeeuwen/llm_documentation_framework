#### ScopedReadLock()


 ScopedReadLock::ScopedReadLock ( const ReadWriteLock & lock ) explicitnoexcept 
 

Creates a ScopedReadLock.As soon as it is created, this will call ReadWriteLock::enterRead(), and when the ScopedReadLock object is deleted, the ReadWriteLock will be unlocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.