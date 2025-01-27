#### remove()


template<class ElementType , class TypeOfCriticalSectionToUse = DummyCriticalSection> 

 ElementType SortedSet< ElementType, TypeOfCriticalSectionToUse >::remove ( const int indexToRemove ) noexcept 
 

Removes an element from the set.This will remove the element at a given index. If the index passed in is outofrange, nothing will happen.Parameters

 indexToRemove the index of the element to remove 
 



Returnsthe element that has been removed 
See alsoremoveValue, removeRange