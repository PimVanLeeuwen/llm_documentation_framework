#### withBottom()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::withBottom ( ValueType newBottom ) const nodiscardnoexcept 
 

Returns a new rectangle with a different bottom edge position, but the same top edge as this one.If the new y is beyond the bottom of the current rectangle, the height will be set to zero.See alsosetBottom References jmax(), and jmin().