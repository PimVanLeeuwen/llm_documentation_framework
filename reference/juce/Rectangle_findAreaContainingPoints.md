#### findAreaContainingPoints()


template<typename ValueType > 

 static Rectangle Rectangle< ValueType >::findAreaContainingPoints ( const Point< ValueType > \* points, int numPoints ) staticnoexcept 
 

Returns the smallest Rectangle that can contain a set of points.References jmax(), jmin(), x, and y.Referenced by Parallelogram< ValueType >::getBoundingBox().