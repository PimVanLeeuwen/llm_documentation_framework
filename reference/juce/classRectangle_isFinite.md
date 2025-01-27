#### isFinite()


template<typename ValueType > 

 bool Rectangle< ValueType >::isFinite ( ) const noexcept 
 

Returns true if the rectangle's values are all finite numbers, i.e.not NaN or infinity.References juce\_isfinite().Referenced by RectangleList< ValueType >::add(), RectangleList< ValueType >::addWithoutMerging(), RectangleList< ValueType >::clipTo(), and RectangleList< ValueType >::getIntersectionWith().