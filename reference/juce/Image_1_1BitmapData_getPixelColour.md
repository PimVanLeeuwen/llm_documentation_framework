#### getPixelColour()


 Colour Image::BitmapData::getPixelColour ( int x, int y ) const noexcept 
 

Returns the colour of a given pixel.For performance reasons, this won't do any boundschecking on the coordinates, so it's the caller's responsibility to make sure they're within the image's size.