#### remove()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::remove ( int indexToRemove ) 
 

Removes an object from the array.This will remove the object at a given index and move back all the subsequent objects to close the gap.If the index passed in is outofrange, nothing will happen.The object that is removed will have its reference count decreased, and may be deleted if not referenced from elsewhere.Parameters

 indexToRemove the index of the element to remove 
 



See alsoremoveObject, removeRange References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), isPositiveAndBelow(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeLast(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject().