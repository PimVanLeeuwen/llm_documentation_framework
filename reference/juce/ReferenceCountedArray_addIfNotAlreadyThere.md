#### addIfNotAlreadyThere() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addIfNotAlreadyThere ( const ObjectClassPtr & newObject ) 
 

Appends a new object at the end of the array as long as the array doesn't already contain it.If the array already contains a matching object, nothing will be done.Parameters

 newObject the new object to add to the array 
 



Returnstrue if the object has been added, false otherwise References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addIfNotAlreadyThere(), and ReferenceCountedObjectPtr< ObjectType >::get().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addIfNotAlreadyThere().