#### transformPoints() [2/2]


template<typename ValueType > 

 void AffineTransform::transformPoints ( ValueType & x1, ValueType & y1, ValueType & x2, ValueType & y2, ValueType & x3, ValueType & y3 ) const noexcept 
 

Transforms three 2D coordinates using this matrix.This is just a shortcut for calling transformPoint() on each of these pairs of coordinates in turn. (And putting all the calculations into one function hopefully also gives the compiler a bit more scope for pipelining it).