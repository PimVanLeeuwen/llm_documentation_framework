#### removeAndReturn()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeAndReturn ( int indexToRemove ) 
 

Removes and returns an object from the array without deleting it.This will remove the object at a given index and return it, moving back all the subsequent objects to close the gap. If the index passed in is outofrange, nothing will happen.Parameters

 indexToRemove the index of the element to remove 
 



See alsoremove, removeObject, removeRange References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), isPositiveAndBelow(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().