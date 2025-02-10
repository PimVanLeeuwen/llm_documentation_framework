#### removeLast()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeLast ( int howManyToRemove = 1 ) 
 

Removes the last n objects from the array.The objects that are removed will have their reference counts decreased, and may be deleted if not referenced from elsewhere.Parameters

 howManyToRemove how many objects to remove from the end of the array 
 



See alsoremove, removeObject, removeRange References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::remove().