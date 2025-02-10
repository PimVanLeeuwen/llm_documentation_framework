#### findNearestProportionalPositionTo()


template<typename ValueType > 

 ValueType Line< ValueType >::findNearestProportionalPositionTo ( Point< ValueType > point ) const noexcept 
 

Finds the point on this line which is nearest to a given point, and returns its position as a proportional position along the line.Returnsa value 0 to 1.0 which is the distance along this line from the line's start to the point which is nearest to the point passedin. To turn this number into a position, use getPointAlongLineProportionally(). 
See alsogetDistanceFromPoint, getPointAlongLineProportionally References jlimit().Referenced by Line< ValueType >::findNearestPointTo().