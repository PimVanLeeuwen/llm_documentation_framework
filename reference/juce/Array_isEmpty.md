#### isEmpty()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 bool Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::isEmpty ( ) const noexcept 
 

Returns true if the array is empty, false otherwise.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size().Referenced by SparseSet< Type >::getTotalRange(), SparseSet< Type >::isEmpty(), dsp::Polynomial< FloatingType >::Polynomial(), and dsp::Polynomial< FloatingType >::Polynomial().