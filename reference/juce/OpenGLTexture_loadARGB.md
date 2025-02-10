#### loadARGB()


 void OpenGLTexture::loadARGB ( const PixelARGB \* pixels, 
 
 int width, 
 int height ) 

Creates a texture from a raw array of pixels.If width and height are not powersoftwo, the texture will be created with a larger size, and only the subsection (0, 0, width, height) will be initialised. The data is sent directly to the OpenGL driver without being flipped vertically, so the first pixel will be mapped onto texture coordinate (0, 0).