#### withTop()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::withTop ( ValueType newTop ) const nodiscardnoexcept 
 

Returns a new rectangle with a different y position, but the same bottom edge as this one.If the new y is beyond the bottom of the current rectangle, the height will be set to zero.See alsosetTop References jmax().Referenced by Rectangle< ValueType >::withTrimmedTop().