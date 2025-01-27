#### setPixelColour()


 void Image::BitmapData::setPixelColour ( int x, int y, Colour colour ) const noexcept 
 

Sets the colour of a given pixel.For performance reasons, this won't do any boundschecking on the coordinates, so it's the caller's responsibility to make sure they're within the image's size.