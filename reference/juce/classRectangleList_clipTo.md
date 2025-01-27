#### clipTo() [2/2]


template<typename ValueType > 
template<typename OtherValueType > 

 bool RectangleList< ValueType >::clipTo ( const RectangleList< OtherValueType > & other ) 
 

Removes any areas of the region that lie outside a given rectangle list.Any rectangles in this object which overlap the specified list will be clipped and subdivided if necessary.Returns true if the resulting region is not empty, false if it is empty.See alsogetIntersectionWith References RectangleList< ValueType >::isEmpty(), and RectangleList< ValueType >::swapWith().