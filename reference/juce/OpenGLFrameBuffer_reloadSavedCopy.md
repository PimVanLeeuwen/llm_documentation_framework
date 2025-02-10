#### reloadSavedCopy()


 bool OpenGLFrameBuffer::reloadSavedCopy ( OpenGLContext & context ) 
 

Restores the framebuffer content that was previously saved using saveAndRelease().After saving to main memory, the original state can be restored by calling restoreToGPUMemory().