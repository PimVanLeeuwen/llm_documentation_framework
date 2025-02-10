#### drawImageTransformed()


 void Graphics::drawImageTransformed ( const Image & imageToDraw, 
 
 const AffineTransform & transform, 
 bool fillAlphaChannelWithCurrentBrush = false ) const 

Draws an image, having applied an affine transform to it.This lets you throw the image around in some wacky ways, rotate it, shear, scale it, etc.Images are composited using the context's current opacity, so if you don't want it to be drawn semitransparently, be sure to call setOpacity (1.0f) (or setColour() with an opaque colour) before drawing images.If fillAlphaChannelWithCurrentBrush is set to true, then the image's RGB channels are ignored and it is filled with the current brush, masked by its alpha channel.If you want to render only a subsection of an image, use Image::getClippedImage() to create the section that you need.See alsosetImageResamplingQuality, drawImage