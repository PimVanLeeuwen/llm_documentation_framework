#### findMinMax()


template<typename Type > 

 Range< Type > AudioBuffer< Type >::findMinMax ( int channel, int startSample, int numSamples ) const noexcept 
 

Returns a Range indicating the lowest and highest sample values in a given section.Parameters

 channel the channel to read from 
 
 startSample the start sample within the channel 
 numSamples the number of samples to check 


References isPositiveAndBelow(), and jassert.Referenced by AudioBuffer< Type >::getMagnitude().