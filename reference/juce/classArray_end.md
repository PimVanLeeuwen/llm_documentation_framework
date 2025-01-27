#### end() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 const ElementType \* Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::end ( ) const noexcept 
 

Returns a pointer to the element which follows the last element in the array.This method is provided for compatibility with standard C++ iteration mechanisms.