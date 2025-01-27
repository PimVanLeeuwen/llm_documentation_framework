#### setTargetValue()


template<typename FloatType > 

 void dsp::LogRampedValue< FloatType >::setTargetValue ( FloatType newValue ) noexcept 
 

Set a new target value.Parameters

 newValue The new target value 
 


References approximatelyEqual(), SmoothedValueBase< LogRampedValue< FloatType > >::countdown, SmoothedValueBase< LogRampedValue< FloatType > >::currentValue, SmoothedValueBase< LogRampedValue< FloatType > >::setCurrentAndTargetValue(), and SmoothedValueBase< LogRampedValue< FloatType > >::target.