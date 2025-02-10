#### findPointerTo()


template<class ObjectType > 

 LinkedListPointer \* LinkedListPointer< ObjectType >::findPointerTo ( ObjectType \*const itemToLookFor ) noexcept 
 

Finds a pointer to a given item.If the item is found in the list, this returns the pointer that points to it. If the item isn't found, this returns null.Referenced by LinkedListPointer< ObjectType >::remove().