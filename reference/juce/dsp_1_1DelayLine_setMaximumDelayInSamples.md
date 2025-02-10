#### setMaximumDelayInSamples()


template<typename SampleType , typename InterpolationType = DelayLineInterpolationTypes::Linear> 

 void dsp::DelayLine< SampleType, InterpolationType >::setMaximumDelayInSamples ( int maxDelayInSamples ) 
 

Sets a new maximum delay in samples.Also clears the delay line.This may allocate internally, so you should never call it from the audio thread.