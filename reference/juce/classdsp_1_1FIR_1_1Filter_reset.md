#### reset()


template<typename SampleType > 

 void dsp::FIR::Filter< SampleType >::reset ( ) 
 

Resets the filter's processing pipeline, ready to start a new stream of data.Note that this clears the processing state, but the type of filter and its coefficients aren't changed. To disable the filter, call setEnabled (false).References dsp::FIR::Filter< SampleType >::coefficients, HeapBlock< ElementType, throwOnFailure >::getData(), jmax(), HeapBlock< ElementType, throwOnFailure >::malloc(), and snapPointerToAlignment().Referenced by dsp::FIR::Filter< SampleType >::Filter(), dsp::FIR::Filter< SampleType >::Filter(), and dsp::FIR::Filter< SampleType >::prepare().