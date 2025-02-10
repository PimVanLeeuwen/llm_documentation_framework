#### makeCopyOf()


template<typename Type > 
template<typename OtherType > 

 void AudioBuffer< Type >::makeCopyOf ( const AudioBuffer< OtherType > & other, 
 
 bool avoidReallocating = false ) 

Resizes this buffer to match the given one, and copies all of its content across.The source buffer can contain a different floating point type, so this can be used to convert between 32 and 64 bit float buffer types.The hasBeenCleared method will return false after this call if the other buffer contains data.References AudioBuffer< Type >::clear(), AudioBuffer< Type >::getNumChannels(), AudioBuffer< Type >::getNumSamples(), AudioBuffer< Type >::getReadPointer(), AudioBuffer< Type >::hasBeenCleared(), and AudioBuffer< Type >::setSize().