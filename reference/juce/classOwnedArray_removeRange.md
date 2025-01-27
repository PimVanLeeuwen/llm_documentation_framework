#### removeRange()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeRange ( int startIndex, 
 
 int numberToRemove, 
 bool deleteObjects = true ) 

Removes a range of objects from the array.This will remove a set of objects, starting from the given index, and move any subsequent elements down to close the gap.If the range extends beyond the bounds of the array, it will be safely clipped to the size of the array.Parameters

 startIndex the index of the first object to remove 
 
 numberToRemove how many objects should be removed 
 deleteObjects whether to delete the objects that get removed 



See alsoremove, removeObject References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addArray(), ContainerDeletePolicy< ObjectType >::destroy(), OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), jlimit(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().Referenced by OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeLast().