#### makeLowShelf()


template<typename NumericType > 

 static std::array< NumericType, 6 > dsp::IIR::ArrayCoefficients< NumericType >::makeLowShelf ( double sampleRate, NumericType cutOffFrequency, NumericType Q, NumericType gainFactor ) static 
 

Returns the coefficients for a lowpass shelf filter with variable Q and gain.The gain is a scale factor that the low frequencies are multiplied by, so values greater than 1.0 will boost the low frequencies, values less than 1.0 will attenuate them.