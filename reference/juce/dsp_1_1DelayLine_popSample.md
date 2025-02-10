#### popSample()


template<typename SampleType , typename InterpolationType = DelayLineInterpolationTypes::Linear> 

 SampleType dsp::DelayLine< SampleType, InterpolationType >::popSample ( int channel, 
 
 SampleType delayInSamples = 1, 
 bool updateReadPointer = true ) 

Pops a single sample from one channel of the delay line.Use this function to modulate the delay in real time or implement standard delay effects with feedback.Parameters

 channel the target channel for the delay line. 
 
 delayInSamples sets the wanted fractional delay in samples, or 1 to use the value being used before or set with setDelay function. 
 updateReadPointer should be set to true if you use the function once for each sample, or false if you need multitap delay capabilities. 



See alsosetDelay, pushSample, process Referenced by dsp::DelayLine< SampleType, InterpolationType >::process().