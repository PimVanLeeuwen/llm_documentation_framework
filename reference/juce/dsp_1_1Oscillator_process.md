#### process()


template<typename SampleType > 
template<typename ProcessContext > 

 void dsp::Oscillator< SampleType >::process ( const ProcessContext & context ) noexcept 
 

Processes the input and output buffers supplied in the processing context.References dsp::Phase< Type >::advance(), SmoothedValue< FloatType, SmoothingType >::getNextValue(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getRawDataPointer(), dsp::Oscillator< SampleType >::isInitialised(), SmoothedValueBase< SmoothedValueType >::isSmoothing(), jassert, jmin(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::size(), and SmoothedValue< FloatType, SmoothingType >::skip().