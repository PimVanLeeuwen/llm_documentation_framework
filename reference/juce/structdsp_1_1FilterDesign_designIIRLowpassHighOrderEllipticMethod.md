#### designIIRLowpassHighOrderEllipticMethod()


template<typename FloatType > 

 static ReferenceCountedArray< IIRCoefficients > dsp::FilterDesign< FloatType >::designIIRLowpassHighOrderEllipticMethod ( FloatType frequency, double sampleRate, FloatType normalisedTransitionWidth, FloatType passbandAmplitudedB, FloatType stopbandAmplitudedB ) static 
 

This method returns an array of IIR::Coefficients, made to be used in cascaded IIR::Filters, providing a minimum phase lowpass filter with ripples in both the pass band and in the stop band.The algorithms are based on "Lecture Notes on Elliptic Filter Design" by Sophocles J. Orfanidis.Parameters

 frequency the cutoff frequency of the lowpass filter 
 
 sampleRate the sample rate being used in the filter design 
 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 passbandAmplitudedB the highest amplitude in dB expected in the pass band (must be negative) 
 stopbandAmplitudedB the lowest amplitude in dB expected in the stop band (must be negative)