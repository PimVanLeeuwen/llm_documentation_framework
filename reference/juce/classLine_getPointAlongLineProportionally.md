#### getPointAlongLineProportionally()


template<typename ValueType > 

 Point< ValueType > Line< ValueType >::getPointAlongLineProportionally ( typename Point< ValueType >::FloatType proportionOfLength ) const noexcept 
 

Returns the location of the point which is a given distance along this line proportional to the line's length.Parameters

 proportionOfLength the distance to move along the line from its start point, in multiples of the line's length. So a value of 0.0 will return the line's start point and a value of 1.0 will return its end point. (This value can be negative or greater than 1.0). 
 



See alsogetPointAlongLine Referenced by Line< ValueType >::findNearestPointTo().