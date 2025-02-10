#### getLast()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ObjectClassPtr ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLast ( ) const noexcept 
 

Returns a pointer to the last object in the array.This will return a null pointer if the array's empty.See alsogetFirst References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().