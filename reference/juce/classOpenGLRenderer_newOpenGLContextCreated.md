#### newOpenGLContextCreated()


 virtual void OpenGLRenderer::newOpenGLContextCreated ( ) pure virtual 
 

Called when a new GL context has been created.You can use this as an opportunity to create your textures, shaders, etc. When the method is invoked, the new GL context will be active. Note that this callback will be made on a background thread, so make sure that your implementation is threadsafe.