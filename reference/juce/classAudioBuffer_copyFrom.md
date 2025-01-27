#### copyFrom() [3/3]


template<typename Type > 

 void AudioBuffer< Type >::copyFrom ( int destChannel, int destStartSample, const Type \* source, int numSamples, Type gain ) noexcept 
 

Copies samples from an array of floats into one of the channels, applying a gain to it.The hasBeenCleared method will return false after this call if samples have been copied.Parameters

 destChannel the channel within this buffer to copy the samples to 
 
 destStartSample the start sample within this buffer's channel 
 source the source buffer to read from 
 numSamples the number of samples to process 
 gain the gain to apply 



See alsoaddFrom References isPositiveAndBelow(), and jassert.