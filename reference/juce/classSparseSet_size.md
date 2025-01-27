#### size()


template<class Type > 

 Type SparseSet< Type >::size ( ) const noexcept 
 

Returns the number of values in the set.Because of the way the data is stored, this method can take longer if there are a lot of items in the set. Use isEmpty() for a quick test of whether there are any items.