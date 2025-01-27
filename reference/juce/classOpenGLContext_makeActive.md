#### makeActive()


 bool OpenGLContext::makeActive ( ) const noexcept 
 

Makes this context the currently active one.You should never need to call this in normal use the context will already be active when OpenGLRenderer::renderOpenGL() is invoked.