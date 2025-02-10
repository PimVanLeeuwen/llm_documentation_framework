#### process()


template<typename ProcessContext , std::enable\_if\_t< std::is\_same\_v< typename ProcessContext::SampleType, float >, int > = 0> 

 void dsp::Convolution::process ( const ProcessContext & context ) noexcept 
 

Performs the filter operation on the given set of samples with optional stereo processing.