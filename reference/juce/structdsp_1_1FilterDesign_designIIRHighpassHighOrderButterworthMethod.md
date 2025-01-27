#### designIIRHighpassHighOrderButterworthMethod()


template<typename FloatType > 

 static ReferenceCountedArray< IIRCoefficients > dsp::FilterDesign< FloatType >::designIIRHighpassHighOrderButterworthMethod ( FloatType frequency, double sampleRate, int order ) static 
 

This method returns an array of IIR::Coefficients, made to be used in cascaded IIRFilters, providing a minimum phase highpass filter without any ripple in the pass band and in the stop band.Parameters

 frequency the cutoff frequency of the highpass filter 
 
 sampleRate the sample rate being used in the filter design 
 order the order of the resulting IIR filter, providing an attenuation of 6 dB times order / octave