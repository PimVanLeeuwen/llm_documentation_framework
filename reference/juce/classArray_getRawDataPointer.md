#### getRawDataPointer() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 const ElementType \* Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getRawDataPointer ( ) const noexcept 
 

Returns a pointer to the actual array data.This pointer will only be valid until the next time a nonconst method is called on the array.