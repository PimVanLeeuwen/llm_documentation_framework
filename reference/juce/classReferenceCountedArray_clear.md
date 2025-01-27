#### clear()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::clear ( ) 
 

Removes all objects from the array.Any objects in the array whose reference counts drop to zero will be deleted.References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::clearQuick(), and ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().