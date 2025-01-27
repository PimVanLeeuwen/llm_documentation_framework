#### ensureAllocatedSize()


template<class ElementType , class TypeOfCriticalSectionToUse > 

 void ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::ensureAllocatedSize ( int minNumElements ) 
 

Increases the amount of storage allocated if it is less than a given amount.This will retain any data currently held in the array, but will add extra space at the end to make sure there it's at least as big as the size passed in. If it's already bigger, no action is taken.Parameters

 minNumElements the minimum number of elements that are needed 
 


References ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::elements, jassert, ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::numAllocated, and ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::setAllocatedSize().