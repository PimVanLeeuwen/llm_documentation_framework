#### getLinePointer()


 uint8 \* Image::BitmapData::getLinePointer ( int y ) const noexcept 
 

Returns a pointer to the start of a line in the image.The coordinate you provide here isn't checked, so it's the caller's responsibility to make sure it's not outofrange.References y.