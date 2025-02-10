#### removeFirstMatchingValue()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeFirstMatchingValue ( ParameterType valueToRemove ) 
 

Removes an item from the array.This will remove the first occurrence of the given element from the array. If the item isn't found, no action is taken.Parameters

 valueToRemove the object to try to remove 
 



Returnsthe index of the removed item, or 1 if the item isn't found 
See alsoremove, removeRange, removeIf References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().