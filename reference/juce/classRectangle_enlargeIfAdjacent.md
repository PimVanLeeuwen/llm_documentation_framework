#### enlargeIfAdjacent()


template<typename ValueType > 

 bool Rectangle< ValueType >::enlargeIfAdjacent ( Rectangle< ValueType > other ) noexcept 
 

If this rectangle merged with another one results in a simple rectangle, this will set this rectangle to the result, and return true.Returns false and does nothing to this rectangle if the two rectangles don't overlap, or if they form a complex region.References exactlyEqual(), Rectangle< ValueType >::getBottom(), Rectangle< ValueType >::getRight(), jmax(), and jmin().