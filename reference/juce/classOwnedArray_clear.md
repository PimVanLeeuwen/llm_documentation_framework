#### clear()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::clear ( bool deleteObjects = true ) 
 

Clears the array, optionally deleting the objects inside it first.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::clearQuick(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeLast().