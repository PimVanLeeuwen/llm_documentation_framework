#### designFIRLowpassWindowMethod()


template<typename FloatType > 

 static FIRCoefficientsPtr dsp::FilterDesign< FloatType >::designFIRLowpassWindowMethod ( FloatType frequency, double sampleRate, size\_t order, WindowingMethod type, FloatType beta = static\_cast< FloatType >(2) ) static 
 

This method generates a FIR::Coefficients for a lowpass filter, using the windowing design method, applied to a sinc impulse response.It is one of the simplest method used to generate a high order lowpass filter, which has the downside of needing more coefficients than more complex method to perform a given attenuation in the stop band.It generates linear phase filters coefficients.Note: The flatTop WindowingMethod generates an impulse response with a maximum amplitude higher than one, and might be normalised if necessary depending on the applications.Parameters

 frequency the cutoff frequency of the lowpass filter 
 
 sampleRate the sample rate being used in the filter design 
 order the order of the filter 
 type the type, must be a WindowingFunction::WindowingType 
 beta an optional additional parameter useful for the Kaiser windowing function