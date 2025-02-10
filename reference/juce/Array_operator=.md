#### operator=() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 Array & Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::operator= ( Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize > && other ) noexcept 
 

References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().