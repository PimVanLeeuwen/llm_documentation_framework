#### setAllocatedSize()


template<class ElementType , class TypeOfCriticalSectionToUse > 

 void ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::setAllocatedSize ( int numElements ) 
 

Changes the amount of storage allocated.This will retain any data currently held in the array, and either add or remove extra space at the end.Parameters

 numElements the number of elements that are needed 
 


References ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::elements, and ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::numAllocated.Referenced by ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::ensureAllocatedSize(), and ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::shrinkToNoMoreThan().