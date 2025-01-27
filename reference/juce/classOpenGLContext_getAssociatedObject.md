#### getAssociatedObject()


 ReferenceCountedObject \* OpenGLContext::getAssociatedObject ( const char \* name ) const 
 

This retrieves an object that was previously stored with setAssociatedObject().If no object is found with the given name, this will return nullptr. This method must only be called from within the GL rendering methods.See alsosetAssociatedObject