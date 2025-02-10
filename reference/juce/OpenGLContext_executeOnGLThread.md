#### executeOnGLThread()


template<typename T > 

 void OpenGLContext::executeOnGLThread ( T && functor, 
 
 bool blockUntilFinished ) 

Execute a lambda, function or functor on the OpenGL thread with an active context.This method will attempt to execute functor on the OpenGL thread. If blockUntilFinished is true then the method will block until the functor has finished executing.This function can only be called if the context is attached to a component. Otherwise, this function will assert.This function is useful when you need to execute housekeeping tasks such as allocating, deallocating textures or framebuffers. As such, the functor will execute without locking the message thread. Therefore, it is not intended for any drawing commands or GUI code. Any GUI code should be executed in the OpenGLRenderer::renderOpenGL callback instead.