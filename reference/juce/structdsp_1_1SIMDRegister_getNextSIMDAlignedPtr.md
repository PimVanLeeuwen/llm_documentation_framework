#### getNextSIMDAlignedPtr()


template<typename Type > 

 static ElementType \* dsp::SIMDRegister< Type >::getNextSIMDAlignedPtr ( ElementType \* ptr ) staticnoexcept 
 

Returns the next position in memory where isSIMDAligned returns true.If the current position in memory is already aligned then this method will simply return the pointer.References dsp::SIMDRegister< Type >::SIMDRegisterSize, and snapPointerToAlignment().

Member Data Documentation