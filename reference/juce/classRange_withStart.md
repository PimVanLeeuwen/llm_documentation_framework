#### withStart()


template<typename ValueType > 

 Range Range< ValueType >::withStart ( const ValueType newStart ) const nodiscardconstexprnoexcept 
 

Returns a range with the same end as this one, but a different start.If the new start position is higher than the current end of the range, the end point will be pushed along to equal it, returning an empty range at the new position.References jmax(), and Range< ValueType >::Range().