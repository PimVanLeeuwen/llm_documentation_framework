#### fill()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::fill ( const ParameterType & newValue ) noexcept 
 

Fills the Array with the provided value.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getLock().