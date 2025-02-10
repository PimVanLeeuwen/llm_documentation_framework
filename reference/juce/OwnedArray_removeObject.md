#### removeObject()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject ( const ObjectClass \* objectToRemove, 
 
 bool deleteObject = true ) 

Removes a specified object from the array.If the item isn't found, no action is taken.Parameters

 objectToRemove the object to try to remove 
 
 deleteObject whether to delete the object (if it's found) 



See alsoremove, removeRange References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::remove().