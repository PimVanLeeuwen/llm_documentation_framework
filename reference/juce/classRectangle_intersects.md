#### intersects() [2/2]


template<typename ValueType > 

 bool Rectangle< ValueType >::intersects ( const Line< ValueType > & line ) const noexcept 
 

Returns true if any part of the given line lies inside this rectangle.References Rectangle< ValueType >::contains(), Rectangle< ValueType >::getBottomLeft(), Rectangle< ValueType >::getBottomRight(), Rectangle< ValueType >::getTopLeft(), and Rectangle< ValueType >::getTopRight().