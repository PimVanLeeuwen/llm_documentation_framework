#### getAspectRatio()


template<typename ValueType > 

 ValueType Rectangle< ValueType >::getAspectRatio ( bool widthOverHeight = true ) const noexcept 
 

Returns the aspect ratio of the rectangle's width / height.If widthOverHeight is true, it returns width / height; if widthOverHeight is false, it returns height / width.