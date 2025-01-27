#### addOversamplingStage()


template<typename SampleType > 

 void dsp::Oversampling< SampleType >::addOversamplingStage ( FilterType , 
 
 float normalisedTransitionWidthUp, 
 float stopbandAmplitudedBUp, 
 float normalisedTransitionWidthDown, 
 float stopbandAmplitudedBDown ) 

Adds a new oversampling stage to the Oversampling class, multiplying the current oversampling factor by two.This is used with the default constructor to create custom oversampling chains, requiring a call to the clearOversamplingStages before any addition.Note: Upsampling and downsampling filtering have different purposes, the former removes upsampling artefacts while the latter removes useless frequency content created by the oversampled process, so usually the attenuation is increased when upsampling compared to downsampling.Parameters

 normalisedTransitionWidthUp a value between 0 and 0.5 which specifies how much the transition between passband and stopband is steep, for upsampling filtering (the lower the better) 
 
 stopbandAmplitudedBUp the amplitude in dB in the stopband for upsampling filtering, must be negative 
 normalisedTransitionWidthDown a value between 0 and 0.5 which specifies how much the transition between passband and stopband is steep, for downsampling filtering (the lower the better) 
 stopbandAmplitudedBDown the amplitude in dB in the stopband for downsampling filtering, must be negative 



See alsoclearOversamplingStages