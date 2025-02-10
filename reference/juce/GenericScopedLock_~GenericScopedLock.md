#### ~GenericScopedLock()


template<class LockType > 

 GenericScopedLock< LockType >::~GenericScopedLock ( ) noexcept 
 

Destructor.The lock will be released when the destructor is called. Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!