#### subtract() [2/2]


template<typename ValueType > 

 bool RectangleList< ValueType >::subtract ( const RectangleList< ValueType > & otherList ) 
 

Removes all areas in another RectangleList from this one.Any rectangles in the list which overlap this will be clipped and subdivided if necessary.Returnstrue if the resulting list is nonempty. References RectangleList< ValueType >::isEmpty(), and RectangleList< ValueType >::subtract().