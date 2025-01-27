#### getDistanceFromPoint()


template<typename ValueType > 

 ValueType Line< ValueType >::getDistanceFromPoint ( Point< ValueType > targetPoint, Point< ValueType > & pointOnLine ) const noexcept 
 

Returns the smallest distance between this line segment and a given point.So if the point is close to the line, this will return the perpendicular distance from the line; if the point is a long way beyond one of the line's endpoint's, it'll return the straightline distance to the nearest endpoint.pointOnLine receives the position of the point that is found.Returnsthe point's distance from the line 
See alsogetPositionAlongLineOfNearestPoint