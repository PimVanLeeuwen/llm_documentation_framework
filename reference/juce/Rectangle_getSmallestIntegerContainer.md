#### getSmallestIntegerContainer()


template<typename ValueType > 

 Rectangle< int > Rectangle< ValueType >::getSmallestIntegerContainer ( ) const noexcept 
 

Returns the smallest integeraligned rectangle that completely contains this one.This is only relevant for floatingpoint rectangles, of course.See alsotoFloat(), toNearestInt(), toNearestIntEdges(), getLargestIntegerWithin() References Rectangle< ValueType >::leftTopRightBottom().