#### setPixelAt()


 void Image::setPixelAt ( int x, 
 
 int y, 
 Colour colour ) 

Sets the colour of one of the image's pixels.If the coordinates are beyond the image's boundaries, then nothing will happen.Note that this won't do any alphablending, it'll just replace the existing pixel with the given one. The colour's opacity will be ignored if this image doesn't have an alphachannel.See alsogetPixelAt, Image::BitmapData::setPixelColour