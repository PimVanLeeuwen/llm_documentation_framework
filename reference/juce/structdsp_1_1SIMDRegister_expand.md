#### expand()


template<typename Type > 

 static SIMDRegister JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::expand ( ElementType s ) staticnoexcept 
 

Creates a new SIMDRegister from the corresponding scalar primitive.The scalar is extended to all elements of the vector.Referenced by dsp::SIMDRegister< Type >::abs(), and dsp::SIMDRegister< Type >::operator==().