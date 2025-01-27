#### coefficients


template<typename SampleType > 

 CoefficientsPtr dsp::IIR::Filter< SampleType >::coefficients 
 

The coefficients of the IIR filter.It's up to the caller to ensure that these coefficients are modified in a threadsafe way.If you change the order of the coefficients then you must call reset after modifying them.