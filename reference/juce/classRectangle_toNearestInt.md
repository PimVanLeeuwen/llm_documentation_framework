#### toNearestInt()


template<typename ValueType > 

 Rectangle< int > Rectangle< ValueType >::toNearestInt ( ) const noexcept 
 

Casts this rectangle to a Rectangle<int>.This uses roundToInt to snap x, y, width and height to the nearest integer (losing precision). If the rectangle already uses integers, this will simply return a copy.See alsogetSmallestIntegerContainer(), toNearestIntEdges() References roundToInt().