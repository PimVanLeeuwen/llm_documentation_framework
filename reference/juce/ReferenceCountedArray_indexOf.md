#### indexOf() [2/2]


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 int ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::indexOf ( const ObjectClassPtr & objectToLookFor ) const noexcept 
 

Finds the index of the first occurrence of an object in the array.Parameters

 objectToLookFor the object to look for 
 



Returnsthe index at which the object was found, or 1 if it's not found References ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::indexOf().Referenced by ReferenceCountedArray< ObjectClass, TypeOfCriticalSectionToUse >::indexOf().