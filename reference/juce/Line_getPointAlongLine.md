#### getPointAlongLine() [2/2]


template<typename ValueType > 

 Point< ValueType > Line< ValueType >::getPointAlongLine ( ValueType distanceFromStart, ValueType perpendicularDistance ) const noexcept 
 

Returns a point which is a certain distance along and to the side of this line.This effectively moves a given distance along the line, then another distance perpendicularly to this, and returns the resulting position.Parameters

 distanceFromStart the distance to move along the line from its start point. This value can be negative or longer than the line itself 
 
 perpendicularDistance how far to move sideways from the line. If you're looking along the line from its start towards its end, then a positive value here will move to the right, negative value move to the left. 


References juce\_hypot().