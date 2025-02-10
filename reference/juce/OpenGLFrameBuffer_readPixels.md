#### readPixels()


 bool OpenGLFrameBuffer::readPixels ( PixelARGB \* targetData, 
 
 const Rectangle< int > & sourceArea ) 

Reads an area of pixels from the framebuffer into a 32bit ARGB pixel array.The lineStride is measured as a number of pixels, not bytes pass a stride of 0 to indicate a packed array.