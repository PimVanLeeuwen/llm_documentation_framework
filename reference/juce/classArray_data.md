#### data() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 const ElementType \* Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::data ( ) const noexcept 
 

Returns a pointer to the first element in the array.This method is provided for compatibility with the standard C++ containers.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::begin().