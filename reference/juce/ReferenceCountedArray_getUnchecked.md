#### getUnchecked()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClassPtr ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getUnchecked ( int index ) const noexcept 
 

Returns a pointer to the object at this index in the array, without checking whether the index is inrange.This is a faster and less safe version of operator[] which doesn't check the index passed in, so it can be used when you're sure the index is always going to be legal.References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getObjectPointerUnchecked().