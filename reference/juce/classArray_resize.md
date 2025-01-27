#### resize()


template<typename ElementType , typename TypeOfCriticalSectionToUse = DummyCriticalSection, int minimumAllocatedSize = 0> 

 void Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::resize ( int targetNumItems ) 
 

This will enlarge or shrink the array to the given number of elements, by adding or removing items from its end.If the array is smaller than the given target size, empty elements will be appended until its size is as specified. If its size is larger than the target, items will be removed from its end to shorten it.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::insertMultiple(), jassert, and Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::removeRange().Referenced by dsp::FIR::Coefficients< NumericType >::Coefficients(), and dsp::Oscillator< SampleType >::prepare().