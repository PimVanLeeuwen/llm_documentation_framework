#### saveAndRelease()


 void OpenGLFrameBuffer::saveAndRelease ( ) 
 

If the framebuffer is active, this will save a stashed copy of its contents in main memory, and will release the GL buffer.After saving, the original state can be restored again by calling reloadSavedCopy().