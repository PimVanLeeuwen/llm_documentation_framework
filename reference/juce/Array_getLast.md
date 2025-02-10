#### getLast()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 ElementType Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLast ( ) const noexcept 
 

Returns the last element in the array, or a default value if the array is empty.See alsooperator[], getUnchecked, getFirst References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by SparseSet< Type >::getTotalRange().