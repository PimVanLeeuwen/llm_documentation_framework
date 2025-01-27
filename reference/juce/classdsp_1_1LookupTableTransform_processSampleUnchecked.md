#### processSampleUnchecked()


template<typename FloatType > 

 FloatType dsp::LookupTableTransform< FloatType >::processSampleUnchecked ( FloatType value ) const noexcept 
 

Calculates the approximated value for the given input value without range checking.Use this if you can guarantee that the input value is within the range specified in the constructor or initialise(), otherwise use processSample().Parameters

 value The approximation is calculated for this input value. 
 



ReturnsThe approximated value for the provided input value.
See alsoprocessSample, operator(), operator[] References jassert.Referenced by dsp::LookupTableTransform< FloatType >::operator[](), and dsp::LookupTableTransform< FloatType >::processUnchecked().