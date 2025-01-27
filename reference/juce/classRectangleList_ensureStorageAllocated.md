#### ensureStorageAllocated()


template<typename ValueType > 

 void RectangleList< ValueType >::ensureStorageAllocated ( int minNumRectangles ) 
 

Increases the internal storage to hold a minimum number of rectangles.Calling this before adding a large number of rectangles means that the array won't have to keep dynamically resizing itself as the elements are added, and it'll therefore be more efficient.See alsoArray::ensureStorageAllocated