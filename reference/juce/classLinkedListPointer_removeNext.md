#### removeNext()


template<class ObjectType > 

 ObjectType \* LinkedListPointer< ObjectType >::removeNext ( ) noexcept 
 

Removes the head item from the list.This won't delete the object that is removed, but returns it, so the caller can delete it if necessary.