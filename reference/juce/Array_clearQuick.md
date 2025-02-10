#### clearQuick()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clearQuick ( ) 
 

Removes all elements from the array without freeing the array's allocated storage.See alsoclear References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().Referenced by Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::clear(), and dsp::Polynomial< FloatingType >::getProductWith().