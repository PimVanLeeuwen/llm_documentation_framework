#### setSample()


template<typename Type > 

 void AudioBuffer< Type >::setSample ( int destChannel, int destSample, Type newValue ) noexcept 
 

Sets a sample in the buffer.The channel and index are not checked they are expected to be inrange. If not, an assertion will be thrown, but in a release build, you're into 'undefined behaviour' territory.The hasBeenCleared method will return false after this call.References isPositiveAndBelow(), and jassert.