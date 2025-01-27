#### isPointAbove()


template<typename ValueType > 

 bool Line< ValueType >::isPointAbove ( Point< ValueType > point ) const noexcept 
 

Returns true if the given point lies above this line.The return value is true if the point's y coordinate is less than the y coordinate of this line at the given x (assuming the line extends infinitely in both directions).