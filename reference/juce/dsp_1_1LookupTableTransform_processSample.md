#### processSample()


template<typename FloatType > 

 FloatType dsp::LookupTableTransform< FloatType >::processSample ( FloatType value ) const noexcept 
 

Calculates the approximated value for the given input value with range checking.This can be called with any input values. Outofrange input values will be clipped to the specified input range.If the index is guaranteed to be in range use the faster processSampleUnchecked() instead.Parameters

 value The approximation is calculated for this input value. 
 



ReturnsThe approximated value for the provided input value.
See alsoprocessSampleUnchecked, operator(), operator[] References isPositiveAndBelow(), jassert, and jlimit().Referenced by dsp::LookupTableTransform< FloatType >::operator()(), and dsp::LookupTableTransform< FloatType >::process().