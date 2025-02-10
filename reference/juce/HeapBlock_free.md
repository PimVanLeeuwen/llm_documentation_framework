#### free()


template<class ElementType , bool throwOnFailure = false> 

 void HeapBlock< ElementType, throwOnFailure >::free ( ) noexcept 
 

Frees any currentlyallocated data.This will free the data and reset this object to be a null pointer.Referenced by HeapBlock< ElementType, throwOnFailure >::operator=(), and AudioBuffer< Type >::setDataToReferTo().