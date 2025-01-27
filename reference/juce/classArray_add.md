#### add() [4/4]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<typename... OtherElements> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::add ( ElementType && firstNewElement, 
 
 OtherElements &&... otherElements ) 

Appends multiple new elements at the end of the array.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().