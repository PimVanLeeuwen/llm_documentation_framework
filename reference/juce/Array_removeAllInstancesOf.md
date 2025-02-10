#### removeAllInstancesOf()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeAllInstancesOf ( ParameterType valueToRemove ) 
 

Removes items from the array.This will remove all occurrences of the given element from the array. If no such items are found, no action is taken.Parameters

 valueToRemove the object to try to remove 
 



Returnshow many objects were removed. 
See alsoremove, removeRange, removeIf References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().