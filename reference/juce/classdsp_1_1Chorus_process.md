#### process()


template<typename SampleType > 
template<typename ProcessContext > 

 void dsp::Chorus< SampleType >::process ( const ProcessContext & context ) noexcept 
 

Processes the input and output samples supplied in the processing context.References dsp::AudioBlock< SampleType >::getSubBlock(), AudioBuffer< Type >::getWritePointer(), jassert, and jmax().