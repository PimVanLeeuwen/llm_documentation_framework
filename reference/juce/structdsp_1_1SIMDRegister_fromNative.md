#### fromNative()


template<typename Type > 

 static SIMDRegister JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::fromNative ( vSIMDType a ) staticnoexcept 
 

Creates a new SIMDRegister from the internal SIMD type (for example \_\_mm128 for singleprecision floating point on SSE architectures).