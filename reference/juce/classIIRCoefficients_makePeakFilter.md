#### makePeakFilter()


 static IIRCoefficients IIRCoefficients::makePeakFilter ( double sampleRate, double centreFrequency, double Q, float gainFactor ) staticnoexcept 
 

Returns the coefficients for a peak filter centred around a given frequency, with a variable Q and gain.The gain is a scale factor that the centre frequencies are multiplied by, so values greater than 1.0 will boost the centre frequencies, values less than 1.0 will attenuate them.

Member Data Documentation