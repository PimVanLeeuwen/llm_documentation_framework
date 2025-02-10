#### removeLast()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeLast ( int howManyToRemove = 1, 
 
 bool deleteObjects = true ) 

Removes the last n objects from the array.Parameters

 howManyToRemove how many objects to remove from the end of the array 
 
 deleteObjects whether to also delete the objects that are removed 



See alsoremove, removeObject, removeRange References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::clear(), OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeRange().