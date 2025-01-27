#### getNumSamples()


template<typename Type > 

 int AudioBuffer< Type >::getNumSamples ( ) const noexcept 
 

Returns the number of samples allocated in each of the buffer's channels.See alsogetNumChannels, getReadPointer, getWritePointer Referenced by ADSR::applyEnvelopeToBuffer(), AudioProcessor::getBusBuffer(), AudioBuffer< Type >::makeCopyOf(), and AudioBuffer< Type >::operator=().