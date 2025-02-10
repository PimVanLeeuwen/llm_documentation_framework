#### ensureStorageAllocated()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::ensureStorageAllocated ( int minNumElements ) 
 

Increases the array's internal storage to hold a minimum number of elements.Calling this before adding a large known number of elements means that the array won't have to keep dynamically resizing itself as the elements are added, and it'll therefore be more efficient.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().