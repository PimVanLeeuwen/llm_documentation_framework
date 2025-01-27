#### getIntersection()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::getIntersection ( Rectangle< ValueType > other ) const noexcept 
 

Returns the region that is the overlap between this and another rectangle.If the two rectangles don't overlap, the rectangle returned will be empty.References jmax(), and jmin().