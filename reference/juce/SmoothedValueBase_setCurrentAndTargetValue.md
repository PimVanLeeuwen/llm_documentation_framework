#### setCurrentAndTargetValue()


template<typename SmoothedValueType > 

 void SmoothedValueBase< SmoothedValueType >::setCurrentAndTargetValue ( FloatType newValue ) 
 

Sets the current value and the target value.Parameters

 newValue the new value to take 
 


References SmoothedValueBase< SmoothedValueType >::countdown, SmoothedValueBase< SmoothedValueType >::currentValue, and SmoothedValueBase< SmoothedValueType >::target.Referenced by dsp::Oscillator< SampleType >::setFrequency().