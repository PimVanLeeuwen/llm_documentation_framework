#### writePixels()


 bool OpenGLFrameBuffer::writePixels ( const PixelARGB \* srcData, 
 
 const Rectangle< int > & targetArea ) 

Writes an area of pixels into the framebuffer from a specified pixel array.The lineStride is measured as a number of pixels, not bytes pass a stride of 0 to indicate a packed array.