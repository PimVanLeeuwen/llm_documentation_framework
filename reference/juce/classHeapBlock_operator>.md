#### operator>()


template<class ElementType , bool throwOnFailure = false> 

 ElementType \* HeapBlock< ElementType, throwOnFailure >::operator> ( ) const noexcept 
 

Lets you use indirect calls to the first element in the array.Obviously this will cause problems if the array hasn't been initialised, because it'll be referencing a null pointer.