#### shutdown()


 virtual void OpenGLAppComponent::shutdown ( ) pure virtual 
 

Implement this method to free any GL objects that you created during rendering.The GL context will still be active when this method is called.Note that because the GL context could be destroyed and recreated adhoc by the underlying platform, the shutdown() and initialise() calls could be called multiple times while your app is running. So don't make your code assume that this will only be called once!