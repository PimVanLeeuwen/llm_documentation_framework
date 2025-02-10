#### addFrom() [2/2]


template<typename Type > 

 void AudioBuffer< Type >::addFrom ( int destChannel, int destStartSample, const Type \* source, int numSamples, Type gainToApplyToSource = Type (1) ) noexcept 
 

Adds samples from an array of floats to one of the channels.The hasBeenCleared method will return false after this call if samples have been added.Parameters

 destChannel the channel within this buffer to add the samples to 
 
 destStartSample the start sample within this buffer's channel 
 source the source data to use 
 numSamples the number of samples to process 
 gainToApplyToSource an optional gain to apply to the source samples before they are added to this buffer's samples 



See alsocopyFrom References isPositiveAndBelow(), and jassert.