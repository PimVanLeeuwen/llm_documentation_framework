#### data() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \*const \* ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::data ( ) const noexcept 
 

Returns a pointer to the first element in the array.This method is provided for compatibility with the standard C++ containers.References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::begin().