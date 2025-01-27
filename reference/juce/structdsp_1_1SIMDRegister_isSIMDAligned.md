#### isSIMDAligned()


template<typename Type > 

 static bool dsp::SIMDRegister< Type >::isSIMDAligned ( const ElementType \* ptr ) staticnoexcept 
 

Checks if the given pointer is sufficiently aligned for using SIMD operations.References dsp::SIMDRegister< Type >::SIMDRegisterSize.Referenced by dsp::SIMDRegister< Type >::copyToRawArray(), and dsp::SIMDRegister< Type >::fromRawArray().