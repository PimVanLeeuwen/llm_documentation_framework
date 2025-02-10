#### insertArray()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::insertArray ( int indexToInsertAt, 
 
 ObjectClass \*const \* newObjects, 
 int numberOfElements ) 

Inserts an array of values into this array at a given position.If the index is less than 0 or greater than the size of the array, the new elements will be added to the end of the array. Otherwise, they will be inserted into the array, moving all the later elements along to make room.Parameters

 indexToInsertAt the index at which the first new element should be inserted 
 
 newObjects the new values to add to the array 
 numberOfElements how many items are in the array 



See alsoinsert, add, addSorted, set References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().