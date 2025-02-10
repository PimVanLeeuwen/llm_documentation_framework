#### loadImage()


 void OpenGLTexture::loadImage ( const Image & image ) 
 

Creates a texture from the given image.Note that if the image's dimensions aren't a poweroftwo, the texture may be created with a larger size.The image will be arranged so that its topleft corner is at texture coordinate (0, 1).