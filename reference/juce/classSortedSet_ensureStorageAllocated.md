#### ensureStorageAllocated()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::ensureStorageAllocated ( const int minNumElements ) 
 

Increases the set's internal storage to hold a minimum number of elements.Calling this before adding a large known number of elements means that the set won't have to keep dynamically resizing itself as the elements are added, and it'll therefore be more efficient.