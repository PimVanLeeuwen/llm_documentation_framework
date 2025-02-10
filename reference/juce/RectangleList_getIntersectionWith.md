#### getIntersectionWith()


template<typename ValueType > 

 bool RectangleList< ValueType >::getIntersectionWith ( RectangleType rect, 
 
 RectangleList< ValueType > & destRegion ) const 

Creates a region which is the result of clipping this one to a given rectangle.Unlike the other clipTo method, this one doesn't affect this object it puts the resulting region into the list whose reference is passedin.Returns true if the resulting region is not empty, false if it is empty.See alsoclipTo References RectangleList< ValueType >::clear(), Rectangle< ValueType >::intersectRectangle(), Rectangle< ValueType >::isEmpty(), RectangleList< ValueType >::isEmpty(), Rectangle< ValueType >::isFinite(), and jassert.