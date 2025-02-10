#### removeRange()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeRange ( int startIndex, 
 
 int numberToRemove ) 

Removes a range of objects from the array.This will remove a set of objects, starting from the given index, and move any subsequent elements down to close the gap.If the range extends beyond the bounds of the array, it will be safely clipped to the size of the array.The objects that are removed will have their reference counts decreased, and may be deleted if not referenced from elsewhere.Parameters

 startIndex the index of the first object to remove 
 
 numberToRemove how many objects should be removed 



See alsoremove, removeObject References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addArray(), ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), jlimit(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads().