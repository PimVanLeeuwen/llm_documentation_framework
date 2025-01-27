#### end() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \*const \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::end ( ) const noexcept 
 

Returns a pointer to the element which follows the last element in the array.This method is provided for compatibility with standard C++ iteration mechanisms.