#### designFIRLowpassKaiserMethod()


template<typename FloatType > 

 static FIRCoefficientsPtr dsp::FilterDesign< FloatType >::designFIRLowpassKaiserMethod ( FloatType frequency, double sampleRate, FloatType normalisedTransitionWidth, FloatType amplitudedB ) static 
 

This a variant of the function designFIRLowpassWindowMethod, which allows the user to specify a transition width and a negative gain in dB, to get a lowpass filter using the Kaiser windowing function, with calculated values of the filter order and of the beta parameter, to satisfy the constraints.It generates linear phase filters coefficients.Parameters

 frequency the cutoff frequency of the lowpass filter 
 
 sampleRate the sample rate being used in the filter design 
 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 amplitudedB the maximum amplitude in dB expected in the stop band (must be negative)