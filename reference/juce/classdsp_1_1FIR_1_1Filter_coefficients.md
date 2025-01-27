#### coefficients


template<typename SampleType > 

 Coefficients<NumericType>::Ptr dsp::FIR::Filter< SampleType >::coefficients 
 

The coefficients of the FIR filter.It's up to the caller to ensure that these coefficients are modified in a threadsafe way.If you change the order of the coefficients then you must call reset after modifying them.Referenced by dsp::FIR::Filter< SampleType >::process(), dsp::FIR::Filter< SampleType >::processSample(), and dsp::FIR::Filter< SampleType >::reset().