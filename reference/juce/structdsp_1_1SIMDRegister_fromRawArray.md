#### fromRawArray()


template<typename Type > 

 static SIMDRegister JUCE\_VECTOR\_CALLTYPE dsp::SIMDRegister< Type >::fromRawArray ( const ElementType \* a ) staticnoexcept 
 

Creates a new SIMDRegister from the first SIMDNumElements of a scalar array.References dsp::SIMDRegister< Type >::isSIMDAligned(), and jassert.