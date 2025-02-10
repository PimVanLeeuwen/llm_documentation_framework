#### loadARGBFlipped()


 void OpenGLTexture::loadARGBFlipped ( const PixelARGB \* pixels, 
 
 int width, 
 int height ) 

Creates a texture from a raw array of pixels.This is like loadARGB, but will vertically flip the data so that the first pixel ends up at texture coordinate (0, 1), and if the width and height are not powersoftwo, it will compensate by using a larger texture size.