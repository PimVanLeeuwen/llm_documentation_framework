#### operator Type \*()


template<typename Type > 

 ThreadLocalValue< Type >::operator Type \* ( ) const noexcept 
 

Returns a pointer to this thread's instance of the value.Note that the first time a thread tries to access the value, an instance of the value object will be created so if your value's class has a nontrivial constructor, be aware that this method could invoke it.References ThreadLocalValue< Type >::get().