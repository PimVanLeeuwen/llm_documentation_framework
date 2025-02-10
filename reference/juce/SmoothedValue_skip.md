#### skip()


template<typename FloatType , typename SmoothingType = ValueSmoothingTypes::Linear> 

 FloatType SmoothedValue< FloatType, SmoothingType >::skip ( int numSamples ) noexcept 
 

Skip the next numSamples samples.This is identical to calling getNextValue numSamples times. It returns the new current value.See alsogetNextValue References SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::countdown, SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::currentValue, SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::setCurrentAndTargetValue(), and SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::target.Referenced by dsp::Oscillator< SampleType >::process().