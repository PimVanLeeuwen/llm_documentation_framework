#### intersectRectangles()


template<typename ValueType > 

 static bool Rectangle< ValueType >::intersectRectangles ( ValueType & x1, ValueType & y1, ValueType & w1, ValueType & h1, ValueType x2, ValueType y2, ValueType w2, ValueType h2 ) staticnoexcept 
 

Static utility to intersect two sets of rectangular coordinates.Returns false if the two regions didn't overlap.See alsointersectRectangle References jmax(), jmin(), x, and y.