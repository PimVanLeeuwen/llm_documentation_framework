#### add() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::add ( std::unique\_ptr< ObjectClass > newObject ) 
 

Appends a new object to the end of the array.Note that this object will be deleted by the OwnedArray when it is removed, so be careful not to delete it somewhere else.Also be careful not to add the same object to the array more than once, as this will obviously cause deletion of dangling pointers.Parameters

 newObject the new object to add to the array 
 



Returnsthe new object that was added 
See alsoset, insert, addSorted References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::add().