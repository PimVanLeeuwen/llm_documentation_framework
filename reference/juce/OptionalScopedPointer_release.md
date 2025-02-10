#### release()


template<class ObjectType > 

 ObjectType \* OptionalScopedPointer< ObjectType >::release ( ) noexcept 
 

Removes the current object from this OptionalScopedPointer without deleting it.This will return the current object, and set this OptionalScopedPointer to a null pointer.