#### setLogParameters()


template<typename FloatType > 

 void dsp::LogRampedValue< FloatType >::setLogParameters ( FloatType midPointAmplitudedB, bool rateOfChangeShouldIncrease ) noexcept 
 

Sets the behaviour of the log ramp.Parameters

 midPointAmplitudedB Sets the amplitude of the mid point in decibels, with the target value at 0 dB and the initial value at inf dB 
 
 rateOfChangeShouldIncrease If true then the ramp starts shallow and gets progressively steeper, if false then the ramp is initially steep and flattens out as you approach the target value 


References Decibels::decibelsToGain(), and jassert.