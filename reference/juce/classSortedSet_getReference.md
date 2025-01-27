#### getReference() [2/2]


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 const ElementType & SortedSet< ElementType, TypeOfCriticalSectionToUse >::getReference ( const int index ) const noexcept 
 

Returns a direct reference to one of the elements in the set, without checking the index passed in.Parameters

 index the index of the element being requested (0 is the first element in the array)