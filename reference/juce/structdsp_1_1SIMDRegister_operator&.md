#### operator&() [2/2]


template<typename Type > 

 SIMDRegister JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::operator& ( MaskType s ) const noexcept 
 

Returns a vector where each element is the bitand'd value of the corresponding element in the receiver and the scalar s.References dsp::SIMDRegister< Type >::value.