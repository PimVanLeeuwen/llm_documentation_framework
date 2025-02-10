#### getLock()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 const TypeOfCriticalSectionToUse & SortedSet< ElementType, TypeOfCriticalSectionToUse >::getLock ( ) const noexcept 
 

Returns the CriticalSection that locks this array.To lock, you can call getLock().enter() and getLock().exit(), or preferably use an object of ScopedLockType as an RAII lock for it.