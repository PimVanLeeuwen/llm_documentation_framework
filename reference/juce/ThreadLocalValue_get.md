#### get()


template<typename Type > 

 Type & ThreadLocalValue< Type >::get ( ) const noexcept 
 

Returns a reference to this thread's instance of the value.Note that the first time a thread tries to access the value, an instance of the value object will be created so if your value's class has a nontrivial constructor, be aware that this method could invoke it.References Atomic< Type >::compareAndSetBool(), Atomic< Type >::get(), and Thread::getCurrentThreadId().Referenced by ThreadLocalValue< Type >::operator Type \*(), ThreadLocalValue< Type >::operator\*(), ThreadLocalValue< Type >::operator>(), and ThreadLocalValue< Type >::operator=().