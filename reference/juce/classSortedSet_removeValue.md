#### removeValue()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 void SortedSet< ElementType, TypeOfCriticalSectionToUse >::removeValue ( const ElementType & valueToRemove ) noexcept 
 

Removes an item from the set.This will remove the given element from the set, if it's there.Parameters

 valueToRemove the object to try to remove 
 



See alsoremove, removeRange