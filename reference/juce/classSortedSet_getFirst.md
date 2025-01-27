#### getFirst()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ElementType SortedSet< ElementType, TypeOfCriticalSectionToUse >::getFirst ( ) const noexcept 
 

Returns the first element in the set, or 0 if the set is empty.See alsooperator[], getUnchecked, getLast