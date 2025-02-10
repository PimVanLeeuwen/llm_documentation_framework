#### setEnd()


template<typename ValueType > 

 void Range< ValueType >::setEnd ( const ValueType newEnd ) noexcept 
 

Changes the end position of the range, leaving the start unchanged.If the new end position is below the current start of the range, the start point will be pushed back to equal the new end point.