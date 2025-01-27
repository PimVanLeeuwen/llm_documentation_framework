#### getNumChannels()


template<typename Type > 

 int AudioBuffer< Type >::getNumChannels ( ) const noexcept 
 

Returns the number of channels of audio data that this buffer contains.See alsogetNumSamples, getReadPointer, getWritePointer Referenced by ADSR::applyEnvelopeToBuffer(), AudioBuffer< Type >::makeCopyOf(), AudioBuffer< Type >::operator=(), and operator==().