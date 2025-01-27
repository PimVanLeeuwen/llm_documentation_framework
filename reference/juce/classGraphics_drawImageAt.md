#### drawImageAt()


 void Graphics::drawImageAt ( const Image & imageToDraw, 
 
 int topLeftX, 
 int topLeftY, 
 bool fillAlphaChannelWithCurrentBrush = false ) const 

Draws an image.This will draw the whole of an image, positioning its topleft corner at the given coordinates, and keeping its size the same. This is the simplest image drawing method the others give more control over the scaling and clipping of the images.Images are composited using the context's current opacity, so if you don't want it to be drawn semitransparently, be sure to call setOpacity (1.0f) (or setColour() with an opaque colour) before drawing images.