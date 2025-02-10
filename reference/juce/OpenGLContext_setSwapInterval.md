#### setSwapInterval()


 bool OpenGLContext::setSwapInterval ( int numFramesPerSwap ) 
 

Sets whether the context checks the vertical sync before swapping.The value is the number of frames to allow between bufferswapping. This is fairly systemdependent, but 0 turns off syncing, 1 makes it swap on frameboundaries, and greater numbers indicate that it should swap less often.By default, this will be set to 1.Returns true if it sets the value successfully some platforms won't support this setting.See alsosetContinuousRepainting