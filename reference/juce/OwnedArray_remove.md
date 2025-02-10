#### remove()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::remove ( int indexToRemove, 
 
 bool deleteObject = true ) 

Removes an object from the array.This will remove the object at a given index (optionally also deleting it) and move back all the subsequent objects to close the gap. If the index passed in is outofrange, nothing will happen.Parameters

 indexToRemove the index of the element to remove 
 
 deleteObject whether to delete the object that is removed 



See alsoremoveObject, removeRange References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), isPositiveAndBelow(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().Referenced by OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject().