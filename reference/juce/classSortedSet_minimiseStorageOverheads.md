#### minimiseStorageOverheads()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::minimiseStorageOverheads ( ) noexcept 
 

Reduces the amount of storage being used by the set.Sets typically allocate slightly more storage than they need, and after removing elements, they may have quite a lot of unused space allocated. This method will reduce the amount of allocated storage to a minimum.