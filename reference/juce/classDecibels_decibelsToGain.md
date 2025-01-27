#### decibelsToGain()


template<typename Type > 

 static Type Decibels::decibelsToGain ( Type decibels, Type minusInfinityDb = Type (defaultMinusInfinitydB) ) static 
 

Converts a dBFS value to its equivalent gain level.A gain of 1.0 = 0 dB, and lower gains map onto negative decibel values. Any decibel value lower than minusInfinityDb will return a gain of 0.Referenced by gainWithLowerBound(), dsp::Gain< FloatType >::setGainDecibels(), and dsp::LogRampedValue< FloatType >::setLogParameters().