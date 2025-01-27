#### clear() [3/3]


template<typename Type > 

 void AudioBuffer< Type >::clear ( int channel, int startSample, int numSamples ) noexcept 
 

Clears a specified region of just one channel.For speed, this doesn't check whether the channel and sample number are inrange, so be careful!This method will do nothing if the buffer has been marked as cleared (i.e. the hasBeenCleared method returns true.)See alsohasBeenCleared, setNotClear References isPositiveAndBelow(), and jassert.