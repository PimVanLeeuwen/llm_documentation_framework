#### getRelativePoint()


template<typename ValueType > 
template<typename FloatType > 

 Point< ValueType > Rectangle< ValueType >::getRelativePoint ( FloatType relativeX, FloatType relativeY ) const noexcept 
 

Returns a point within this rectangle, specified as proportional coordinates.The relative X and Y values should be between 0 and 1, where 0 is the left or top of this rectangle, and 1 is the right or bottom. (Outofbounds values will return a point outside the rectangle).