#### applyTransform()


template<typename ValueType > 

 void Point< ValueType >::applyTransform ( const AffineTransform & transform ) noexcept 
 

Uses a transform to change the point's coordinates.This will only compile if ValueType = float!See alsoAffineTransform::transformPoint References x, and y.