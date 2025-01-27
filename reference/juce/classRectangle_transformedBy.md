#### transformedBy()


template<typename ValueType > 

 Rectangle Rectangle< ValueType >::transformedBy ( const AffineTransform & transform ) const nodiscardnoexcept 
 

Returns the smallest rectangle that can contain the shape created by applying a transform to this rectangle.This should only be used on floating point rectangles.References jmax(), jmin(), and Rectangle< ValueType >::Rectangle.