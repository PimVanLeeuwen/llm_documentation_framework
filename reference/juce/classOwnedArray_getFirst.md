#### getFirst()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getFirst ( ) const noexcept 
 

Returns a pointer to the first object in the array.This will return a null pointer if the array's empty.See alsogetLast References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().