#### process()


template<typename SampleType > 
template<typename ProcessContext > 

 void dsp::Compressor< SampleType >::process ( const ProcessContext & context ) noexcept 
 

Processes the input and output samples supplied in the processing context.References jassert, and dsp::Compressor< SampleType >::processSample().