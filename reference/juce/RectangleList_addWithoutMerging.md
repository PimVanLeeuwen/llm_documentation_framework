#### addWithoutMerging()


template<typename ValueType > 

 void RectangleList< ValueType >::addWithoutMerging ( RectangleType rect ) 
 

Dumbly adds a rectangle to the list without checking for overlaps.This simply adds the rectangle to the end, it doesn't merge it or remove any overlapping bits.The rectangle can have any size and may be empty, but if it's floating point then it's expected to not contain any INF values.References Rectangle< ValueType >::isEmpty(), Rectangle< ValueType >::isFinite(), and jassert.Referenced by LowLevelGraphicsContext::drawRect(), and RectangleList< ValueType >::RectangleList().