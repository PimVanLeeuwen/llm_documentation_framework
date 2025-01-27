#### ~GenericScopedUnlock()


template<class LockType > 

 GenericScopedUnlock< LockType >::~GenericScopedUnlock ( ) noexcept 
 

Destructor.The CriticalSection will be unlocked when the destructor is called.Make sure this object is created and deleted by the same thread, otherwise there are no guarantees what will happen!