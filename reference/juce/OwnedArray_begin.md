#### begin() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \*const \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::begin ( ) const noexcept 
 

Returns a pointer to the first element in the array.This method is provided for compatibility with standard C++ iteration mechanisms.