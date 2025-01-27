#### withEnd()


template<typename ValueType > 

 Range Range< ValueType >::withEnd ( const ValueType newEnd ) const nodiscardconstexprnoexcept 
 

Returns a range with the same start position as this one, but a different end.If the new end position is below the current start of the range, the start point will be pushed back to equal the new end point.References jmin(), and Range< ValueType >::Range().