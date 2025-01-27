#### processSample()


template<typename FloatType , typename Function = FloatType (\*) (FloatType)> 
template<typename SampleType > 

 SampleType JUCE\_VECTOR\_CALLTYPE dsp::WaveShaper< FloatType, Function >::processSample ( SampleType inputSample ) const noexcept 
 

Returns the result of processing a single sample.References dsp::WaveShaper< FloatType, Function >::functionToUse.