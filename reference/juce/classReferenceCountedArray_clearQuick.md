#### clearQuick()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::clearQuick ( ) 
 

Removes all objects from the array without freeing the array's allocated storage.Any objects in the array that whose reference counts drop to zero will be deleted.See alsoclear References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::clear().