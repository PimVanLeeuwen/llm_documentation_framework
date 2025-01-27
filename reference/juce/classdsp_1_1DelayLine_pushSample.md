#### pushSample()


template<typename SampleType , typename InterpolationType = DelayLineInterpolationTypes::Linear> 

 void dsp::DelayLine< SampleType, InterpolationType >::pushSample ( int channel, 
 
 SampleType sample ) 

Pushes a single sample into one channel of the delay line.Use this function and popSample instead of process if you need to modulate the delay in real time instead of using a fixed delay value, or if you want to code a delay effect with a feedback loop.See alsosetDelay, popSample, process Referenced by dsp::DelayLine< SampleType, InterpolationType >::process().