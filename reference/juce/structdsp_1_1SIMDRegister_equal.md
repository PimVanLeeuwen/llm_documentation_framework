#### equal()


template<typename Type > 

 static vMaskType JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::equal ( SIMDRegister< Type > a, SIMDRegister< Type > b ) staticnoexcept 
 

Returns a SIMDRegister of the corresponding integral type where each element has each bit set if the corresponding element of a is equal to the corresponding element of b, or zero otherwise.The result can then be used in bit operations defined above to avoid branches in vector SIMD code.