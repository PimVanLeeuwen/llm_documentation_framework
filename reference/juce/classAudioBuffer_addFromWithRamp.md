#### addFromWithRamp()


template<typename Type > 

 void AudioBuffer< Type >::addFromWithRamp ( int destChannel, int destStartSample, const Type \* source, int numSamples, Type startGain, Type endGain ) noexcept 
 

Adds samples from an array of floats, applying a gain ramp to them.The hasBeenCleared method will return false after this call if samples have been added.Parameters

 destChannel the channel within this buffer to add the samples to 
 
 destStartSample the start sample within this buffer's channel 
 source the source data to use 
 numSamples the number of samples to process 
 startGain the gain to apply to the first sample (this is multiplied with the source samples before they are added to this buffer) 
 endGain The gain that would apply to the sample after the final sample. The gain that applies to the final sample is (numSamples 1) / numSamples \* (endGain startGain). This ensures a continuous ramp when supplying the same value in endGain and startGain in subsequent blocks. The gain is linearly interpolated between the first and last samples. 


References isPositiveAndBelow(), and jassert.