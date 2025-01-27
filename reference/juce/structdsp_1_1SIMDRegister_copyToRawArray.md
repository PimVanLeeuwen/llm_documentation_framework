#### copyToRawArray()


template<typename Type > 

 void JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::copyToRawArray ( ElementType \* a ) const noexcept 
 

Copies the elements of the SIMDRegister to a scalar array in memory.References dsp::SIMDRegister< Type >::isSIMDAligned(), jassert, and dsp::SIMDRegister< Type >::value.