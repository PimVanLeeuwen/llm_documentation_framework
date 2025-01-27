#### getLargestIntegerWithin()


template<typename ValueType > 

 Rectangle< int > Rectangle< ValueType >::getLargestIntegerWithin ( ) const noexcept 
 

Returns the largest integeraligned rectangle that is completely contained by this one.Returns an empty rectangle, outside the original rectangle, if no integeraligned rectangle is contained by this one. This is only relevant for floatingpoint rectangles, of course.See alsotoFloat(), toNearestInt(), toNearestIntEdges(), getSmallestIntegerContainer() References jmax().