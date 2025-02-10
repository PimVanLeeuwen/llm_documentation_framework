#### getIntersectionWith()


template<typename ValueType > 

 Range Range< ValueType >::getIntersectionWith ( Range< ValueType > other ) const nodiscardconstexprnoexcept 
 

Returns the range that is the intersection of the two ranges, or an empty range with an undefined start position if they don't overlap.References jmax(), jmin(), and Range< ValueType >::Range().Referenced by Reservoir::doBufferedRead().