#### reset() [2/2]


template<typename FloatType , typename SmoothingType = ValueSmoothingTypes::Linear> 

 void SmoothedValue< FloatType, SmoothingType >::reset ( int numSteps ) noexcept 
 

Set a new ramp length directly in samples.Parameters

 numSteps The number of samples over which the ramp should be active 
 


References SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::setCurrentAndTargetValue(), and SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::target.