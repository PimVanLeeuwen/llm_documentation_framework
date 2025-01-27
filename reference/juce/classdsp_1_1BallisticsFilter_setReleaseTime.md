#### setReleaseTime()


template<typename SampleType > 

 void dsp::BallisticsFilter< SampleType >::setReleaseTime ( SampleType releaseTimeMs ) 
 

Sets the release time in ms.Release times less than 0.001 ms will be snapped to zero and very long release times will eventually saturate depending on the numerical precision used.