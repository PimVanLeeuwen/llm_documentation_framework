#### process()


template<typename SampleType > 
template<typename ProcessContext > 

 void dsp::BallisticsFilter< SampleType >::process ( const ProcessContext & context ) noexcept 
 

Processes the input and output samples supplied in the processing context.References jassert, dsp::BallisticsFilter< SampleType >::processSample(), and dsp::BallisticsFilter< SampleType >::snapToZero().