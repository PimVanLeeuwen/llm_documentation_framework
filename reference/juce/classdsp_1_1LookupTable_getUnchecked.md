#### getUnchecked()


template<typename FloatType > 

 FloatType dsp::LookupTable< FloatType >::getUnchecked ( FloatType index ) const noexcept 
 

Calculates the approximated value for the given index without range checking.Use this if you can guarantee that the index is nonnegative and less than numPoints. Otherwise use get().Parameters

 index The approximation is calculated for this noninteger index. 
 



ReturnsThe approximated value at the given index.
See alsoget, operator[] References dsp::LookupTable< FloatType >::getNumPoints(), Array< ElementType, TypeOfCriticalSectionToUse, minimumAllocatedSize >::getUnchecked(), dsp::LookupTable< FloatType >::isInitialised(), isPositiveAndBelow(), jassert, jmap(), and truncatePositiveToUnsignedInt().Referenced by dsp::LookupTable< FloatType >::get(), and dsp::LookupTable< FloatType >::operator[]().