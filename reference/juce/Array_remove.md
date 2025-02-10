#### remove() [2/2]


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::remove ( const ElementType \* elementToRemove ) 
 

Removes an element from the array.This will remove the element pointed to by the given iterator, and move back all the subsequent elements to close the gap. If the iterator passed in does not point to an element within the array, behaviour is undefined.Parameters

 elementToRemove a pointer to the element to remove 
 



See alsoremoveFirstMatchingValue, removeAllInstancesOf, removeRange, removeIf References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), isPositiveAndBelow(), jassert, and jassertfalse.