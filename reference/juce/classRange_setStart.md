#### setStart()


template<typename ValueType > 

 void Range< ValueType >::setStart ( const ValueType newStart ) noexcept 
 

Changes the start position of the range, leaving the end position unchanged.If the new start position is higher than the current end of the range, the end point will be pushed along to equal it, leaving an empty range at the new position.Referenced by Reservoir::doBufferedRead().