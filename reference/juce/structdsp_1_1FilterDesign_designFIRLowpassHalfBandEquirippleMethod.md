#### designFIRLowpassHalfBandEquirippleMethod()


template<typename FloatType > 

 static FIRCoefficientsPtr dsp::FilterDesign< FloatType >::designFIRLowpassHalfBandEquirippleMethod ( FloatType normalisedTransitionWidth, FloatType amplitudedB ) static 
 

This method generates a FIR::Coefficients for a lowpass filter, with a cutoff frequency at half band, using an algorithm described in the article "Design of HalfBand FIR Filters for Signal Compression" from Pavel Zahradnik, to get an equiripple like high order FIR filter, without the need of an iterative method and convergence failure risks.It generates linear phase filters coefficients.Parameters

 normalisedTransitionWidth the normalised size between 0 and 0.5 of the transition between the pass band and the stop band 
 
 amplitudedB the maximum amplitude in dB expected in the stop band (must be negative)