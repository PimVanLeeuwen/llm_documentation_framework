#### getRenderingScale()


 double OpenGLContext::getRenderingScale ( ) const noexcept 
 

Returns a scale factor that relates the context component's size to the number of physical pixels it covers on the screen.In special cases it will be the same as Displays::Display::scale, but it also includes AffineTransforms that affect the rendered area, and will be correctly reported not just in standalone applications but plugins as well.Note that this should only be called during an OpenGLRenderer::renderOpenGL() callback at other times the value it returns is undefined.