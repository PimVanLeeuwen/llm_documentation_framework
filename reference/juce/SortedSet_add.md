#### add()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 bool SortedSet< ElementType, TypeOfCriticalSectionToUse >::add ( const ElementType & newElement ) noexcept 
 

Adds a new element to the set, (as long as it's not already in there).Note that if a matching element already exists, the new value will be assigned to the existing one using operator=, so that if there are any differences between the objects which were not recognised by the object's operator==, then the set will always contain a copy of the most recently added one.Parameters

 newElement the new object to add to the set 
 



Returnstrue if the value was added, or false if it already existed 
See alsoset, insert, addIfNotAlreadyThere, addSorted, addSet, addArray