#### designFIRLowpassTransitionMethod()


template<typename FloatType > 

 static FIRCoefficientsPtr dsp::FilterDesign< FloatType >::designFIRLowpassTransitionMethod ( FloatType frequency, double sampleRate, size\_t order, FloatType normalisedTransitionWidth, FloatType spline ) static 
 

This method is also a variant of the function designFIRLowpassWindowMethod, using a rectangular window as a basis, and a spline transition between the pass band and the stop band, to reduce the Gibbs phenomenon.It generates linear phase filters coefficients.Parameters

 frequency the cutoff frequency of the lowpass filter 
 
 sampleRate the sample rate being used in the filter design 
 order the order of the filter 
 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 spline between 1.0 and 4.0, indicates how much the transition is curved, with 1.0 meaning a straight line