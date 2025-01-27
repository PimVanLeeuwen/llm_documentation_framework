#### makeBandPass() [2/2]


template<typename NumericType > 

 static std::array< NumericType, 6 > dsp::IIR::ArrayCoefficients< NumericType >::makeBandPass ( double sampleRate, NumericType frequency, NumericType Q ) static 
 

Returns the coefficients for a bandpass filter with variable Q.