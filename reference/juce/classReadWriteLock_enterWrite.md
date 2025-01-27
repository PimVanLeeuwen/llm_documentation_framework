#### enterWrite()


 void ReadWriteLock::enterWrite ( ) const noexcept 
 

Locks this object for writing.This will block until any other threads that have it locked for reading or writing have released their lock.See alsoexitWrite, ScopedWriteLock