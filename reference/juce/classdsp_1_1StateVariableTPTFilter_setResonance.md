#### setResonance()


template<typename SampleType > 

 void dsp::StateVariableTPTFilter< SampleType >::setResonance ( SampleType newResonance ) 
 

Sets the resonance of the filter.Note: The bandwidth of the resonance increases with the value of the parameter. To have a standard 12 dB / octave filter, the value must be set at 1 / sqrt (2).