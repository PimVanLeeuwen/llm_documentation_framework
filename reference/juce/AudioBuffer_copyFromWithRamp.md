#### copyFromWithRamp()


template<typename Type > 

 void AudioBuffer< Type >::copyFromWithRamp ( int destChannel, int destStartSample, const Type \* source, int numSamples, Type startGain, Type endGain ) noexcept 
 

Copies samples from an array of floats into one of the channels, applying a gain ramp.The hasBeenCleared method will return false after this call if samples have been copied.Parameters

 destChannel the channel within this buffer to copy the samples to 
 
 destStartSample the start sample within this buffer's channel 
 source the source buffer to read from 
 numSamples the number of samples to process 
 startGain the gain to apply to the first sample (this is multiplied with the source samples before they are copied to this buffer) 
 endGain The gain that would apply to the sample after the final sample. The gain that applies to the final sample is (numSamples 1) / numSamples \* (endGain startGain). This ensures a continuous ramp when supplying the same value in endGain and startGain in subsequent blocks. The gain is linearly interpolated between the first and last samples. 



See alsoaddFrom References isPositiveAndBelow(), and jassert.