#### append()


template<class ObjectType > 

 void LinkedListPointer< ObjectType >::append ( ObjectType \*const newItem ) 
 

Adds an item to the end of the list.This operation involves iterating the whole list, so can be slow if you need to append a number of items to your list, it's much more efficient to use the Appender class than to repeatedly call append().References LinkedListPointer< ObjectType >::getLast().