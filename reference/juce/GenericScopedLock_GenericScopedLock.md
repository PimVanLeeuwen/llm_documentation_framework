#### GenericScopedLock()


template<class LockType > 

 GenericScopedLock< LockType >::GenericScopedLock ( const LockType & lock ) explicitnoexcept 
 

Creates a GenericScopedLock.As soon as it is created, this will acquire the lock, and when the GenericScopedLock object is deleted, the lock will be released.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen! Best just to use it as a local stack object, rather than creating one with the new() operator.