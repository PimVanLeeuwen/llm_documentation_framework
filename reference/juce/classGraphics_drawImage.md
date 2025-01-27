#### drawImage() [2/2]


 void Graphics::drawImage ( const Image & imageToDraw, 
 
 Rectangle< float > targetArea, 
 RectanglePlacement placementWithinTarget = RectanglePlacement::stretchToFit, 
 bool fillAlphaChannelWithCurrentBrush = false ) const 

Draws an image to fit within a designated rectangle.Parameters

 imageToDraw the source image to draw 
 
 targetArea the target rectangle to fit it into 
 placementWithinTarget this specifies how the image should be positioned within the target rectangle see the RectanglePlacement class for more details about this. 
 fillAlphaChannelWithCurrentBrush if true, then instead of drawing the image, just its alpha channel will be used as a mask with which to draw with the current brush or colour. This is similar to fillAlphaMap(), and see also drawImage() 



See alsodrawImage, drawImageTransformed, drawImageAt, RectanglePlacement