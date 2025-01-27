#### leftTopRightBottom()


template<typename ValueType > 

 static Rectangle Rectangle< ValueType >::leftTopRightBottom ( ValueType left, ValueType top, ValueType right, ValueType bottom ) staticnoexcept 
 

Creates a Rectangle from a set of left, right, top, bottom coordinates.The right and bottom values must be larger than the left and top ones, or the resulting rectangle will have a negative size.Referenced by Rectangle< ValueType >::getSmallestIntegerContainer(), and Rectangle< ValueType >::toNearestIntEdges().