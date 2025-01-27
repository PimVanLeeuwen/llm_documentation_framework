#### toNearestIntEdges()


template<typename ValueType > 

 Rectangle< int > Rectangle< ValueType >::toNearestIntEdges ( ) const noexcept 
 

Casts this rectangle to a Rectangle<int>.This uses roundToInt to snap top, left, right and bottom to the nearest integer (losing precision). If the rectangle already uses integers, this will simply return a copy.See alsogetSmallestIntegerContainer(), toNearestInt() References Rectangle< ValueType >::getBottom(), Rectangle< ValueType >::getRight(), Rectangle< ValueType >::leftTopRightBottom(), and roundToInt().