#### reduceIfPartlyContainedIn()


template<typename ValueType > 

 bool Rectangle< ValueType >::reduceIfPartlyContainedIn ( Rectangle< ValueType > other ) noexcept 
 

If after removing another rectangle from this one the result is a simple rectangle, this will set this object's bounds to be the result, and return true.Returns false and does nothing to this rectangle if the two rectangles don't overlap, or if removing the other one would form a complex region.