#### addArray()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::addArray ( const ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse > & arrayToAddFrom, int startIndex = 0, int numElementsToAdd = 1 ) noexcept 
 

Adds elements from another array to the end of this array.Parameters

 arrayToAddFrom the array from which to copy the elements 
 
 startIndex the first element of the other array to start copying from 
 numElementsToAdd how many elements to add from the other array. If this value is negative or greater than the number of available elements, all available elements will be copied. 



See alsoadd References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().