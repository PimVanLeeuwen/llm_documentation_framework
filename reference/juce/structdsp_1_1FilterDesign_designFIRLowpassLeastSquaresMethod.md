#### designFIRLowpassLeastSquaresMethod()


template<typename FloatType > 

 static FIRCoefficientsPtr dsp::FilterDesign< FloatType >::designFIRLowpassLeastSquaresMethod ( FloatType frequency, double sampleRate, size\_t order, FloatType normalisedTransitionWidth, FloatType stopBandWeight ) static 
 

This method generates a FIR::Coefficients for a lowpass filter, by minimizing the average error between the generated filter and an ideal one using the least squares error criterion and matrices operations.It generates linear phase filters coefficients.Parameters

 frequency the cutoff frequency of the lowpass filter 
 
 sampleRate the sample rate being used in the filter design 
 order the order of the filter 
 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 stopBandWeight between 1.0 and 100.0, indicates how much we want attenuation in the stop band, against some oscillation in the pass band