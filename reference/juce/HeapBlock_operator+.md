#### operator+()


template<class ElementType , bool throwOnFailure = false> 
template<typename IndexType > 

 ElementType \* HeapBlock< ElementType, throwOnFailure >::operator+ ( IndexType index ) const noexcept 
 

Returns a pointer to a data element at an offset from the start of the array.This is the same as doing pointer arithmetic on the raw pointer itself.