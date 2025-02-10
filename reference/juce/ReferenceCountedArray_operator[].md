#### operator[]()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClassPtr ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::operator[] ( int index ) const noexcept 
 

Returns a pointer to the object at this index in the array.If the index is outofrange, this will return a null pointer, (and it could be null anyway, because it's ok for the array to hold null pointers as well as objects).See alsogetUnchecked References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getObjectPointer().