#### getRMSLevel()


template<typename Type > 

 Type AudioBuffer< Type >::getRMSLevel ( int channel, int startSample, int numSamples ) const noexcept 
 

Returns the root mean squared level for a region of a channel.References isPositiveAndBelow(), and jassert.