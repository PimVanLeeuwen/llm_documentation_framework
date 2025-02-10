#### indexOf()


template<class ObjectClass , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 int OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::indexOf ( const ObjectClass \* objectToLookFor ) const noexcept 
 

Finds the index of an object which might be in the array.Parameters

 objectToLookFor the object to look for 
 



Returnsthe index at which the object was found, or 1 if it's not found References OwnedArray< ObjectClass, TypeOfCriticalSectionToUse >::getLock().