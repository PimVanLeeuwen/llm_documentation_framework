#### openGLContextClosing()


 virtual void OpenGLRenderer::openGLContextClosing ( ) pure virtual 
 

Called when the current openGL context is about to close.You can use this opportunity to release any GL resources that you may have created.Note that this callback will be made on a background thread, so make sure that your implementation is threadsafe.(Also note that on Android, this callback won't happen, because there's currently no way to implement it..)