#### getUnchecked()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ElementType SortedSet< ElementType, TypeOfCriticalSectionToUse >::getUnchecked ( const int index ) const noexcept 
 

Returns one of the elements in the set, without checking the index passed in.Unlike the operator[] method, this will try to return an element without checking that the index is within the bounds of the set, so should only be used when you're confident that it will always be a valid index.Parameters

 index the index of the element being requested (0 is the first element in the set) 
 



See alsooperator[], getFirst, getLast