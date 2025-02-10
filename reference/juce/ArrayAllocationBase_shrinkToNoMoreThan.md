#### shrinkToNoMoreThan()


template<class ElementType , class TypeOfCriticalSectionToUse > 

 void ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::shrinkToNoMoreThan ( int maxNumElements ) 
 

Minimises the amount of storage allocated so that it's no more than the given number of elements.References ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::numAllocated, and ArrayAllocationBase< ElementType, TypeOfCriticalSectionToUse >::setAllocatedSize().