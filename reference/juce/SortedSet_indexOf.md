#### indexOf()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 int SortedSet< ElementType, TypeOfCriticalSectionToUse >::indexOf ( const ElementType & elementToLookFor ) const noexcept 
 

Finds the index of the first element which matches the value passed in.This will search the set for the given object, and return the index of its first occurrence. If the object isn't found, the method will return 1.Parameters

 elementToLookFor the value or object to look for 
 



Returnsthe index of the object, or 1 if it's not found