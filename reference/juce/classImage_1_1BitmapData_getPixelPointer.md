#### getPixelPointer()


 uint8 \* Image::BitmapData::getPixelPointer ( int x, int y ) const noexcept 
 

Returns a pointer to a pixel in the image.The coordinates you give here are not checked, so it's the caller's responsibility to make sure they're not outofrange.References x, and y.