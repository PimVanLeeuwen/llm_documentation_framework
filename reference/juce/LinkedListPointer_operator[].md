#### operator[]() [2/2]


template<class ObjectType > 

 const LinkedListPointer & LinkedListPointer< ObjectType >::operator[] ( int index ) const noexcept 
 

Returns the item at a given index in the list.Since the only way to find an item is to iterate the list, this operation can obviously be slow, depending on its size, so you should be careful when using this in algorithms.