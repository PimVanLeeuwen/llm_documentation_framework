#### transformAll()


template<typename ValueType > 

 void RectangleList< ValueType >::transformAll ( const AffineTransform & transform ) noexcept 
 

Applies a transform to all the rectangles.Obviously this will create a mess if the transform involves any rotation or skewing.