#### operator const void \*()


template<class ElementType , bool throwOnFailure = false> 

 HeapBlock< ElementType, throwOnFailure >::operator const void \* ( ) const noexcept 
 

Returns a void pointer to the allocated data.This may be a null pointer if the data hasn't yet been allocated, or if it has been freed by calling the free() method.