#### insertAtIndex()


template<class ObjectType > 

 void LinkedListPointer< ObjectType >::insertAtIndex ( int index, 
 
 ObjectType \* newItem ) 

Inserts an item at a numeric index in the list.Obviously this will involve iterating the list to find the item at the given index, so be careful about the impact this may have on execution time.References jassert.