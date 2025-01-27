#### getLast()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClass \* OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLast ( ) const noexcept 
 

Returns a pointer to the last object in the array.This will return a null pointer if the array's empty.See alsogetFirst References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().