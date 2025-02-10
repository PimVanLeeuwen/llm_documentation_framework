#### getPixelAt()


 Colour Image::getPixelAt ( int x, 
 
 int y ) const 

Returns the colour of one of the pixels in the image.If the coordinates given are beyond the image's boundaries, this will return Colours::transparentBlack.See alsosetPixelAt, Image::BitmapData::getPixelColour