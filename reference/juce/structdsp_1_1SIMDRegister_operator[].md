#### operator[]() [2/2]


template<typename Type > 

 ElementAccess JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::operator[] ( size\_t idx ) noexcept 
 

Returns the idxth element of the receiver.Note that this does not check if idx is larger than the native register size.References jassert, and dsp::SIMDRegister< Type >::SIMDNumElements.