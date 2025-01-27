#### operator[]()


template<class ElementType , bool throwOnFailure = false> 
template<typename IndexType > 

 ElementType & HeapBlock< ElementType, throwOnFailure >::operator[] ( IndexType index ) const noexcept 
 

Returns a reference to one of the data elements.Obviously there's no boundschecking here, as this object is just a dumb pointer and has no idea of the size it currently has allocated.