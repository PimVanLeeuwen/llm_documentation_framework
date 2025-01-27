#### get()


template<typename Type > 

 Type Atomic< Type >::get ( ) const noexcept 
 

Atomically reads and returns the current value.References Atomic< Type >::value.Referenced by ThreadLocalValue< Type >::get(), ThreadLocalValue< Type >::releaseCurrentThreadStorage(), and ThreadLocalValue< Type >::~ThreadLocalValue().