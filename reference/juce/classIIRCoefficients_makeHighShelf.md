#### makeHighShelf()


 static IIRCoefficients IIRCoefficients::makeHighShelf ( double sampleRate, double cutOffFrequency, double Q, float gainFactor ) staticnoexcept 
 

Returns the coefficients for a highpass shelf filter with variable Q and gain.The gain is a scale factor that the high frequencies are multiplied by, so values greater than 1.0 will boost the high frequencies, values less than 1.0 will attenuate them.