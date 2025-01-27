#### operator[]()


template<class Type > 

 Type SparseSet< Type >::operator[] ( Type index ) const noexcept 
 

Returns one of the values in the set.Parameters

 index the index of the value to retrieve, in the range 0 to (size() 1). 
 



Returnsthe value at this index, or 0 if it's outofrange References end().