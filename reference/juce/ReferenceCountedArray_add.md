#### add() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::add ( const ObjectClassPtr & newObject ) 
 

Appends a new object to the end of the array.This will increase the new object's reference count.Parameters

 newObject the new object to add to the array 
 



See alsoset, insert, addIfNotAlreadyThere, addSorted, addArray References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::add(), and ReferenceCountedObjectPtr< ObjectType >::get().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::add().