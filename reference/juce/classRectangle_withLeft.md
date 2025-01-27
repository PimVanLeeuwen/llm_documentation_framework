#### withLeft()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::withLeft ( ValueType newLeft ) const nodiscardnoexcept 
 

Returns a new rectangle with a different x position, but the same righthand edge as this one.If the new x is beyond the right of the current righthand edge, the width will be set to zero.See alsosetLeft References jmax().Referenced by Rectangle< ValueType >::withTrimmedLeft().