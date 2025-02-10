#### applyEnvelopeToBuffer()


template<typename FloatType > 

 void ADSR::applyEnvelopeToBuffer ( AudioBuffer< FloatType > & buffer, 
 
 int startSample, 
 int numSamples ) 

This method will conveniently apply the next numSamples number of envelope values to an AudioBuffer.See alsogetNextSample References AudioBuffer< Type >::applyGain(), AudioBuffer< Type >::clear(), AudioBuffer< Type >::getNumChannels(), AudioBuffer< Type >::getNumSamples(), AudioBuffer< Type >::getWritePointer(), and jassert.