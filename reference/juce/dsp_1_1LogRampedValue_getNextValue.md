#### getNextValue()


template<typename FloatType > 

 FloatType dsp::LogRampedValue< FloatType >::getNextValue ( ) noexcept 
 

Compute the next value.ReturnsSmoothed value References SmoothedValueBase< LogRampedValue< FloatType > >::countdown, SmoothedValueBase< LogRampedValue< FloatType > >::currentValue, SmoothedValueBase< LogRampedValue< FloatType > >::isSmoothing(), jmap(), and SmoothedValueBase< LogRampedValue< FloatType > >::target.