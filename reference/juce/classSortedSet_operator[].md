#### operator[]()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ElementType SortedSet< ElementType, TypeOfCriticalSectionToUse >::operator[] ( const int index ) const noexcept 
 

Returns one of the elements in the set.If the index passed in is beyond the range of valid elements, this will return zero.If you're certain that the index will always be a valid element, you can call getUnchecked() instead, which is faster.Parameters

 index the index of the element being requested (0 is the first element in the set) 
 



See alsogetUnchecked, getFirst, getLast