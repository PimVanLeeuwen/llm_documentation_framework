#### minimiseStorageOverheads()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::minimiseStorageOverheads ( ) noexcept 
 

Reduces the amount of storage being used by the array.Arrays typically allocate slightly more storage than they need, and after removing elements, they may have quite a lot of unused space allocated. This method will reduce the amount of allocated storage to a minimum.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::remove(), OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeAndReturn(), and OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::removeRange().