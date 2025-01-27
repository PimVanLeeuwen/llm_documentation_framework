#### getReference() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 const ElementType & Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getReference ( int index ) const noexcept 
 

Returns a direct reference to one of the elements in the array, without checking the index passed in.This is like getUnchecked, but returns a direct reference to the element. Obviously this can be dangerous, so only use it when absolutely necessary.Parameters

 index the index of the element being requested (0 is the first element in the array) 
 



See alsooperator[], getFirst, getLast References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().