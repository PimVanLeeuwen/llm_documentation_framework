#### getRawDataPointer()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \*\* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getRawDataPointer ( ) noexcept 
 

Returns a pointer to the actual array data.This pointer will only be valid until the next time a nonconst method is called on the array.