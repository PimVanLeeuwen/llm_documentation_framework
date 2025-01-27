#### ensureStorageAllocated()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::ensureStorageAllocated ( int minNumElements ) noexcept 
 

Increases the array's internal storage to hold a minimum number of elements.Calling this before adding a large known number of elements means that the array won't have to keep dynamically resizing itself as the elements are added, and it'll therefore be more efficient.References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().