#### getRawCoefficients() [2/2]


template<typename NumericType > 

 const NumericType \* dsp::FIR::Coefficients< NumericType >::getRawCoefficients ( ) const noexcept 
 

Returns a raw data pointer to the coefficients.References Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::begin(), and dsp::FIR::Coefficients< NumericType >::coefficients.