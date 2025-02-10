#### getObjectPointer()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getObjectPointer ( int index ) const noexcept 
 

Returns a raw pointer to the object at this index in the array.If the index is outofrange, this will return a null pointer, (and it could be null anyway, because it's ok for the array to hold null pointers as well as objects).See alsogetUnchecked References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::operator[]().