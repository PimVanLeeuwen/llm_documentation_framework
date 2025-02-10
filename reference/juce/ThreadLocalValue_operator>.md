#### operator>()


template<typename Type > 

 Type \* ThreadLocalValue< Type >::operator> ( ) const noexcept 
 

Accesses a method or field of the value object.Note that the first time a thread tries to access the value, an instance of the value object will be created so if your value's class has a nontrivial constructor, be aware that this method could invoke it.References ThreadLocalValue< Type >::get().