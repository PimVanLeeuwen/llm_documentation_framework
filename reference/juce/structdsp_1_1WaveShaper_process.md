#### process()


template<typename FloatType , typename Function = FloatType (\*) (FloatType)> 
template<typename ProcessContext > 

 void dsp::WaveShaper< FloatType, Function >::process ( const ProcessContext & context ) const noexcept 
 

Processes the input and output buffers supplied in the processing context.References dsp::WaveShaper< FloatType, Function >::functionToUse, and dsp::AudioBlock< SampleType >::process().