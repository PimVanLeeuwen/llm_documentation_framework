#### insert() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert ( int indexToInsertAt, 
 
 std::unique\_ptr< ObjectClass > newObject ) 

Inserts a new object into the array at the given index.Note that this object will be deleted by the OwnedArray when it is removed, so be careful not to delete it somewhere else.If the index is less than 0 or greater than the size of the array, the element will be added to the end of the array. Otherwise, it will be inserted into the array, moving all the later elements along to make room.Be careful not to add the same object to the array more than once, as this will obviously cause deletion of dangling pointers.Parameters

 indexToInsertAt the index at which the new element should be inserted 
 
 newObject the new object to add to the array 



Returnsthe new object that was added 
See alsoadd, addSorted, set References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::insert().