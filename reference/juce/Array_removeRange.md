#### removeRange()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeRange ( int startIndex, 
 
 int numberToRemove ) 

Removes a range of elements from the array.This will remove a set of elements, starting from the given index, and move subsequent elements down to close the gap.If the range extends beyond the bounds of the array, it will be safely clipped to the size of the array.Parameters

 startIndex the index of the first element to remove 
 
 numberToRemove how many elements should be removed 



See alsoremove, removeFirstMatchingValue, removeAllInstancesOf, removeIf References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), and jlimit().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::resize().