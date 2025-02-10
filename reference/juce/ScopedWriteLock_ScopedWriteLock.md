#### ScopedWriteLock()


 ScopedWriteLock::ScopedWriteLock ( const ReadWriteLock & lock ) explicitnoexcept 
 

Creates a ScopedWriteLock.As soon as it is created, this will call ReadWriteLock::enterWrite(), and when the ScopedWriteLock object is deleted, the ReadWriteLock will be unlocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.