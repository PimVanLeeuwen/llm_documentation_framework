#### renderOpenGL()


 virtual void OpenGLRenderer::renderOpenGL ( ) pure virtual 
 

Called when you should render the next openGL frame.Note that this callback will be made on a background thread.If the context is attached to a component in order to do component rendering, then the MessageManager will be locked when this callback is made.If no component rendering is being done, then the MessageManager will not be locked, and you'll need to make sure your code is threadsafe in any interactions it has with your GUI classes.For information about how to trigger a render callback, see OpenGLContext::triggerRepaint() and OpenGLContext::setContinuousRepainting().IMPORTANT: Never take a MessageManagerLock inside this function! On macOS, the OpenGL context will be locked for the duration of this call. The main thread may also attempt to interact with the OpenGL context at any time, which will also require locking the OpenGL context. As a result, taking a MessageManagerLock inside renderOpenGL() may cause a hierarchical deadlock.