#### gainToDecibels()


template<typename Type > 

 static Type Decibels::gainToDecibels ( Type gain, Type minusInfinityDb = Type (defaultMinusInfinitydB) ) static 
 

Converts a gain level into a dBFS value.A gain of 1.0 = 0 dB, and lower gains map onto negative decibel values. If the gain is 0 (or negative), then the method will return the value provided as minusInfinityDb.References jmax().Referenced by dsp::Gain< FloatType >::getGainDecibels().