#### reset() [2/2]


template<typename FloatType > 

 void dsp::LogRampedValue< FloatType >::reset ( int numSteps ) noexcept 
 

Set a new ramp length directly in samples.Parameters

 numSteps The number of samples over which the ramp should be active 
 


References SmoothedValueBase< LogRampedValue< FloatType > >::setCurrentAndTargetValue(), and SmoothedValueBase< LogRampedValue< FloatType > >::target.