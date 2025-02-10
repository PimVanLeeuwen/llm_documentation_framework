#### insert() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert ( int indexToInsertAt, 
 
 const ObjectClassPtr & newObject ) 

Inserts a new object into the array at the given index.If the index is less than 0 or greater than the size of the array, the element will be added to the end of the array. Otherwise, it will be inserted into the array, moving all the later elements along to make room.This will increase the new object's reference count.Parameters

 indexToInsertAt the index at which the new element should be inserted 
 
 newObject the new object to add to the array 



See alsoadd, addSorted, addIfNotAlreadyThere, set References ReferenceCountedObjectPtr< ObjectType >::get(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert().