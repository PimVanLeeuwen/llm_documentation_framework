#### setAssociatedObject()


 void OpenGLContext::setAssociatedObject ( const char \* name, 
 
 ReferenceCountedObject \* newObject ) 

Attaches a named object to the context, which will be deleted when the context is destroyed.This allows you to store an object which will be released before the context is deleted. The main purpose is for caching GL objects such as shader programs, which will become invalid when the context is deleted.This method must only be called from within the GL rendering methods.