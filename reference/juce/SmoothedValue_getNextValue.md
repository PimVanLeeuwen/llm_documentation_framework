#### getNextValue()


template<typename FloatType , typename SmoothingType = ValueSmoothingTypes::Linear> 

 FloatType SmoothedValue< FloatType, SmoothingType >::getNextValue ( ) noexcept 
 

Compute the next value.ReturnsSmoothed value References SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::countdown, SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::currentValue, SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::isSmoothing(), and SmoothedValueBase< SmoothedValue< FloatType, ValueSmoothingTypes::Linear > >::target.Referenced by dsp::Oscillator< SampleType >::process(), Reverb::processMono(), dsp::Oscillator< SampleType >::processSample(), and Reverb::processStereo().