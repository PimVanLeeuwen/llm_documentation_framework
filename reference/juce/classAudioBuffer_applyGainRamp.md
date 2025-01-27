#### applyGainRamp() [2/2]


template<typename Type > 

 void AudioBuffer< Type >::applyGainRamp ( int startSample, int numSamples, Type startGain, Type endGain ) noexcept 
 

Applies a range of gains to a region of all channels.The gain that is applied to each sample will vary from startGain on the first sample to endGain on the last Sample, so it can be used to do basic fades.For speed, this doesn't check whether the sample numbers are inrange, so be careful!References AudioBuffer< Type >::applyGainRamp().