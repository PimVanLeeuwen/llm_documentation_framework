#### get()


template<typename Type > 

 ElementType JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::get ( size\_t idx ) const noexcept 
 

Returns the idxth element of the receiver.Note that this does not check if idx is larger than the native register size.References jassert, dsp::SIMDRegister< Type >::SIMDNumElements, and dsp::SIMDRegister< Type >::value.Referenced by dsp::SIMDRegister< Type >::operator[]().