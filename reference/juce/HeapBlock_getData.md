#### getData()


template<class ElementType , bool throwOnFailure = false> 

 ElementType \* HeapBlock< ElementType, throwOnFailure >::getData ( ) const noexcept 
 

Returns a raw pointer to the allocated data.This may be a null pointer if the data hasn't yet been allocated, or if it has been freed by calling the free() method.Referenced by dsp::FIR::Filter< SampleType >::reset().