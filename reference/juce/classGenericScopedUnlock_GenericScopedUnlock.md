#### GenericScopedUnlock()


template<class LockType > 

 GenericScopedUnlock< LockType >::GenericScopedUnlock ( const LockType & lock ) explicitnoexcept 
 

Creates a GenericScopedUnlock.As soon as it is created, this will unlock the CriticalSection, and when the ScopedLock object is deleted, the CriticalSection will be relocked.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.