#### copyTexture()


 void OpenGLContext::copyTexture ( const Rectangle< int > & targetClipArea, 
 
 const Rectangle< int > & anchorPosAndTextureSize, 
 int contextWidth, 
 int contextHeight, 
 bool textureOriginIsBottomLeft ) 

Draws the currently selected texture into this context at its original size.Parameters

 targetClipArea the target area to draw into (in topleft origin coords) 
 
 anchorPosAndTextureSize the position of this rectangle is the texture's topleft anchor position in the target space, and the size must be the total size of the texture. 
 contextWidth the width of the context or framebuffer that is being drawn into, used for scaling of the coordinates. 
 contextHeight the height of the context or framebuffer that is being drawn into, used for vertical flipping of the y coordinates. 
 textureOriginIsBottomLeft if true, the texture's origin is treated as being at (0, 0). If false, it is assumed to be (0, 1)