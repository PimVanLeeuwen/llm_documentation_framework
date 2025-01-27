#### sort()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::sort ( ) 
 

Sorts the array using a default comparison operation.If the type of your elements isn't supported by the DefaultElementComparator class then you may need to use the other version of sort, which takes a custom comparator.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::sort().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::sort().