#### removeObject() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject ( const ObjectClassPtr & objectToRemove ) 
 

Removes the first occurrence of a specified object from the array.If the item isn't found, no action is taken. If it is found, it is removed and has its reference count decreased.Parameters

 objectToRemove the object to try to remove 
 



See alsoremove, removeRange References ReferenceCountedObjectPtr< ObjectType >::get(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeObject().