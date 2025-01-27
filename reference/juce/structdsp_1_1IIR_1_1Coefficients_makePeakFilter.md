#### makePeakFilter()


template<typename NumericType > 

 static Ptr dsp::IIR::Coefficients< NumericType >::makePeakFilter ( double sampleRate, NumericType centreFrequency, NumericType Q, NumericType gainFactor ) static 
 

Returns the coefficients for a peak filter centred around a given frequency, with a variable Q and gain.The gain is a scale factor that the centre frequencies are multiplied by, so values greater than 1.0 will boost the centre frequencies, values less than 1.0 will attenuate them.