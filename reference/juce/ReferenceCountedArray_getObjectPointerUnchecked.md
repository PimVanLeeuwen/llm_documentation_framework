#### getObjectPointerUnchecked()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getObjectPointerUnchecked ( int index ) const noexcept 
 

Returns a raw pointer to the object at this index in the array, without checking whether the index is inrange.References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getUnchecked().