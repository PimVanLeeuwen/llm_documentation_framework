#### makeLowShelf()


 static IIRCoefficients IIRCoefficients::makeLowShelf ( double sampleRate, double cutOffFrequency, double Q, float gainFactor ) staticnoexcept 
 

Returns the coefficients for a lowpass shelf filter with variable Q and gain.The gain is a scale factor that the low frequencies are multiplied by, so values greater than 1.0 will boost the low frequencies, values less than 1.0 will attenuate them.