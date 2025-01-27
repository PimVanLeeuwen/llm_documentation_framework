#### getFirst()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 ElementType Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getFirst ( ) const noexcept 
 

Returns the first element in the array, or a default value if the array is empty.See alsooperator[], getUnchecked, getLast References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by SparseSet< Type >::getTotalRange().