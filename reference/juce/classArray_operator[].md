#### operator[]()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 ElementType Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::operator[] ( int index ) const 
 

Returns one of the elements in the array.If the index passed in is beyond the range of valid elements, this will return a default value.If you're certain that the index will always be a valid element, you can call getUnchecked() instead, which is faster.Parameters

 index the index of the element being requested (0 is the first element in the array) 
 



See alsogetUnchecked, getFirst, getLast References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().