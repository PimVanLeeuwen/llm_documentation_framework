#### get()


template<typename FloatType > 

 FloatType dsp::LookupTable< FloatType >::get ( FloatType index ) const noexcept 
 

Calculates the approximated value for the given index with range checking.This can be called with any input indices. If the provided index is outofrange either the bottom or the top element of the LookupTable is returned.If the index is guaranteed to be in range use the faster getUnchecked() instead.Parameters

 index The approximation is calculated for this noninteger index. 
 



ReturnsThe approximated value at the given index.
See alsogetUnchecked, operator[] References dsp::LookupTable< FloatType >::getNumPoints(), and dsp::LookupTable< FloatType >::getUnchecked().