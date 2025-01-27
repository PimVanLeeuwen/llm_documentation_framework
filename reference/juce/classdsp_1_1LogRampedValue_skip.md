#### skip()


template<typename FloatType > 

 FloatType dsp::LogRampedValue< FloatType >::skip ( int numSamples ) noexcept 
 

Skip the next numSamples samples.This is identical to calling getNextValue numSamples times.See alsogetNextValue References SmoothedValueBase< LogRampedValue< FloatType > >::countdown, SmoothedValueBase< LogRampedValue< FloatType > >::currentValue, jmap(), SmoothedValueBase< LogRampedValue< FloatType > >::setCurrentAndTargetValue(), and SmoothedValueBase< LogRampedValue< FloatType > >::target.