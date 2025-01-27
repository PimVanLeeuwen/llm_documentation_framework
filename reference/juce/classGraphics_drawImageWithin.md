#### drawImageWithin()


 void Graphics::drawImageWithin ( const Image & imageToDraw, 
 
 int destX, 
 int destY, 
 int destWidth, 
 int destHeight, 
 RectanglePlacement placementWithinTarget, 
 bool fillAlphaChannelWithCurrentBrush = false ) const 

Draws an image to fit within a designated rectangle.If the image is too big or too small for the space, it will be rescaled to fit as nicely as it can do without affecting its aspect ratio. It will then be placed within the target rectangle according to the justification flags specified.Parameters

 imageToDraw the source image to draw 
 
 destX topleft of the target rectangle to fit it into 
 destY topleft of the target rectangle to fit it into 
 destWidth size of the target rectangle to fit the image into 
 destHeight size of the target rectangle to fit the image into 
 placementWithinTarget this specifies how the image should be positioned within the target rectangle see the RectanglePlacement class for more details about this. 
 fillAlphaChannelWithCurrentBrush if true, then instead of drawing the image, just its alpha channel will be used as a mask with which to draw with the current brush or colour. This is similar to fillAlphaMap(), and see also drawImage() 



See alsosetImageResamplingQuality, drawImage, drawImageTransformed, drawImageAt, RectanglePlacement