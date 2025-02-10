#### containsRectangle()


template<typename ValueType > 

 bool RectangleList< ValueType >::containsRectangle ( RectangleType rectangleToCheck ) const 
 

Checks whether the region contains the whole of a given rectangle.Returnstrue all parts of the rectangle passed in lie within the region defined by this object 
See alsointersectsRectangle, containsPoint References RectangleList< ValueType >::isEmpty(), and RectangleList< ValueType >::subtract().