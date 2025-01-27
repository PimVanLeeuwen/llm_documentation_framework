#### makeHighPass() [2/2]


template<typename NumericType > 

 static std::array< NumericType, 6 > dsp::IIR::ArrayCoefficients< NumericType >::makeHighPass ( double sampleRate, NumericType frequency, NumericType Q ) static 
 

Returns the coefficients for a highpass filter with variable Q.