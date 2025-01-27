#### addSorted()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 
template<class ElementComparator > 

 int Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addSorted ( ElementComparator & comparator, 
 
 ParameterType newElement ) 

Inserts a new element into the array, assuming that the array is sorted.This will use a comparator to find the position at which the new element should go. If the array isn't sorted, the behaviour of this method will be unpredictable.Parameters

 comparator the comparator to use to compare the elements see the sort() method for details about the form this object should take 
 
 newElement the new element to insert to the array 



Returnsthe index at which the new item was added 
See alsoaddUsingDefaultSort, add, sort References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock(), and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insert().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addUsingDefaultSort().