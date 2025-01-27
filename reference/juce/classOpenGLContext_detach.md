#### detach()


 void OpenGLContext::detach ( ) 
 

Detaches the context from its target component and deletes any native resources.If the context has not been attached, this will do nothing. Otherwise, it will block until the context and its thread have been cleaned up.