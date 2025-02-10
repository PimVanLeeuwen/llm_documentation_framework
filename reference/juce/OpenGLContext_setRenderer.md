#### setRenderer()


 void OpenGLContext::setRenderer ( OpenGLRenderer \* ) noexcept 
 

Gives the context an OpenGLRenderer to use to do the drawing.The object that you give it will not be owned by the context, so it's the caller's responsibility to manage its lifetime and make sure that it doesn't get deleted while the context may be using it. To stop the context using a renderer, just call this method with a null pointer. Note: This must be called BEFORE attaching your context to a target component!