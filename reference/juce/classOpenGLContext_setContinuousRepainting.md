#### setContinuousRepainting()


 void OpenGLContext::setContinuousRepainting ( bool shouldContinuouslyRepaint ) noexcept 
 

Enables or disables continuous repainting.If set to true, the context will run a loop, rerendering itself without waiting for triggerRepaint() to be called, at a frequency determined by the swap interval (see setSwapInterval). If false, then after each render callback, it will wait for another call to triggerRepaint() before rendering again. This is disabled by default.See alsosetSwapInterval