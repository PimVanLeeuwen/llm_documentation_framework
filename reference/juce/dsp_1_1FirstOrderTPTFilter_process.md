#### process()


template<typename SampleType > 
template<typename ProcessContext > 

 void dsp::FirstOrderTPTFilter< SampleType >::process ( const ProcessContext & context ) noexcept 
 

Processes the input and output samples supplied in the processing context.References jassert, dsp::FirstOrderTPTFilter< SampleType >::processSample(), and dsp::FirstOrderTPTFilter< SampleType >::snapToZero().