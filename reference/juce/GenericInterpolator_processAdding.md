#### processAdding() [2/2]


template<class InterpolatorTraits , int memorySize> 

 int GenericInterpolator< InterpolatorTraits, memorySize >::processAdding ( double speedRatio, const float \* inputSamples, float \* outputSamples, int numOutputSamplesToProduce, int numInputSamplesAvailable, int wrapAround, float gain ) noexcept 
 

Resamples a stream of samples, adding the results to the output data with a gain.Parameters

 speedRatio the number of input samples to use for each output sample 
 
 inputSamples the source data to read from. This must contain at least (speedRatio \* numOutputSamplesToProduce) samples. 
 outputSamples the buffer to write the results to the result values will be added to any preexisting data in this buffer after being multiplied by the gain factor 
 numOutputSamplesToProduce the number of output samples that should be created 
 numInputSamplesAvailable the number of available input samples. If it needs more samples than available, it either wraps back for wrapAround samples, or it feeds zeroes 
 wrapAround if the stream exceeds available samples, it wraps back for wrapAround samples. If wrapAround is set to 0, it will feed zeroes. 
 gain a gain factor to multiply the resulting samples by before adding them to the destination buffer 



Returnsthe actual number of input samples that were used