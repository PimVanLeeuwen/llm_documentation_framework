#### getMaximumDelayInSamples()


template<typename SampleType , typename InterpolationType = DelayLineInterpolationTypes::Linear> 

 int dsp::DelayLine< SampleType, InterpolationType >::getMaximumDelayInSamples ( ) const noexcept 
 

Gets the maximum possible delay in samples.For very short delay times, the result of getMaximumDelayInSamples() may differ from the last value passed to setMaximumDelayInSamples().