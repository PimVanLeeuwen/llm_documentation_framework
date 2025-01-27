#### loadAlpha()


 void OpenGLTexture::loadAlpha ( const uint8 \* pixels, 
 
 int width, 
 int height ) 

Creates an alphachannel texture from an array of alpha values.If width and height are not powersoftwo, the texture will be created with a larger size, and only the subsection (0, 0, width, height) will be initialised. The data is sent directly to the OpenGL driver without being flipped vertically, so the first pixel will be mapped onto texture coordinate (0, 0).