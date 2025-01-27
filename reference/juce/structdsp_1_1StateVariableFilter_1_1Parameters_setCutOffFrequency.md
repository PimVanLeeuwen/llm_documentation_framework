#### setCutOffFrequency()


template<typename NumericType > 

 void dsp::StateVariableFilter::Parameters< NumericType >::setCutOffFrequency ( double sampleRate, NumericType frequency, NumericType resonance = static\_cast<NumericType> (1.0 / MathConstants<double>::sqrt2) ) noexcept 
 

Sets the cutoff frequency and resonance of the IIR filter.Note: The bandwidth of the resonance increases with the value of the parameter. To have a standard 12 dB/octave filter, the value must be set at 1 / sqrt (2).References dsp::StateVariableFilter::Parameters< NumericType >::g, dsp::StateVariableFilter::Parameters< NumericType >::h, jassert, and dsp::StateVariableFilter::Parameters< NumericType >::R2.