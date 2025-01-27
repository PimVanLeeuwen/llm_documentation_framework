#### removeAndReturn()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 ElementType Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeAndReturn ( int indexToRemove ) 
 

Removes an element from the array.This will remove the element at a given index, and move back all the subsequent elements to close the gap. If the index passed in is outofrange, nothing will happen.Parameters

 indexToRemove the index of the element to remove 
 



Returnsthe element that has been removed 
See alsoremoveFirstMatchingValue, removeAllInstancesOf, removeRange References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), and isPositiveAndBelow().Referenced by SelectedItemSet< SelectableItemType >::deselect(), SelectedItemSet< SelectableItemType >::deselectAll(), and SelectedItemSet< SelectableItemType >::operator=().