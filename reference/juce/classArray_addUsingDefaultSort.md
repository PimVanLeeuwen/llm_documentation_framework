#### addUsingDefaultSort()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addUsingDefaultSort ( ParameterType newElement ) 
 

Inserts a new element into the array, assuming that the array is sorted.This will use the DefaultElementComparator class for sorting, so your ElementType must be suitable for use with that class. If the array isn't sorted, the behaviour of this method will be unpredictable.Parameters

 newElement the new element to insert to the array 
 



See alsoaddSorted, sort References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::addSorted().