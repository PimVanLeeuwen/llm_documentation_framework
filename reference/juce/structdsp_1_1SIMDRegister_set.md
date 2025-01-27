#### set()


template<typename Type > 

 void JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::set ( size\_t idx, ElementType v ) noexcept 
 

Sets the idxth element of the receiver.Note that this does not check if idx is larger than the native register size.References jassert, dsp::SIMDRegister< Type >::SIMDNumElements, and dsp::SIMDRegister< Type >::value.