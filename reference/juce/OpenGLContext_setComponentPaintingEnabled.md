#### setComponentPaintingEnabled()


 void OpenGLContext::setComponentPaintingEnabled ( bool shouldPaintComponent ) noexcept 
 

Enables or disables the use of the GL context to perform 2D rendering of the component to which it is attached.If this is false, then only your OpenGLRenderer will be used to perform any rendering. If true, then each time your target's paint() method needs to be called, an OpenGLGraphicsContext will be used to render it, (after calling your OpenGLRenderer if there is one).By default this is set to true. If you're not using any paint() method functionality and are doing all your rendering in an OpenGLRenderer, you should disable it to improve performance.Note: This must be called BEFORE attaching your context to a target component!