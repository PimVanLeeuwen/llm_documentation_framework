#### removeAndReturn()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClassPtr ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeAndReturn ( int indexToRemove ) 
 

Removes and returns an object from the array.This will remove the object at a given index and return it, moving back all the subsequent objects to close the gap. If the index passed in is outofrange, nothing will happen and a null pointer will be returned.Parameters

 indexToRemove the index of the element to remove 
 



See alsoremove, removeObject, removeRange References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), isPositiveAndBelow(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().