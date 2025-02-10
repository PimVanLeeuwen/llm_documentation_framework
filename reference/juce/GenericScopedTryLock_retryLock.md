#### retryLock()


template<class LockType > 

 bool GenericScopedTryLock< LockType >::retryLock ( ) const noexcept 
 

Retry gaining the lock by calling tryEnter on the underlying lock.