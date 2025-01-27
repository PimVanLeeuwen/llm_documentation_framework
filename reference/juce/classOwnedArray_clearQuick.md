#### clearQuick()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::clearQuick ( bool deleteObjects ) 
 

Clears the array, optionally deleting the objects inside it first.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::clear().