#### setTargetValue()


template<typename FloatType , typename SmoothingType = ValueSmoothingTypes::Linear> 

 void SmoothedValue< FloatType, SmoothingType >::setTargetValue ( FloatType newValue ) noexcept 
 

Set the next value to ramp towards.Parameters

 newValue The new target value 
 


References approximatelyEqual(), SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::countdown, jassert, SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::setCurrentAndTargetValue(), and SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::target.Referenced by dsp::Oscillator< SampleType >::setFrequency(), and Reverb::setParameters().