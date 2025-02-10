#### withRight()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::withRight ( ValueType newRight ) const nodiscardnoexcept 
 

Returns a new rectangle with a different righthand edge position, but the same lefthand edge as this one.If the new right edge is below the current lefthand edge, the width will be set to zero.See alsosetRight References jmax(), and jmin().