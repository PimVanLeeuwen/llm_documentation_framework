#### multiplyAlphaAt()


 void Image::multiplyAlphaAt ( int x, 
 
 int y, 
 float multiplier ) 

Changes the opacity of a pixel.This only has an effect if the image has an alpha channel and if the given coordinates are inside the image's boundary.The multiplier must be in the range 0 to 1.0, and the current alpha at the given coordinates will be multiplied by this value.See alsosetPixelAt