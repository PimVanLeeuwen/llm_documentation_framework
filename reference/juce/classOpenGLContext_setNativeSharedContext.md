#### setNativeSharedContext()


 void OpenGLContext::setNativeSharedContext ( void \* nativeContextToShareWith ) noexcept 
 

Provides a context with which you'd like this context's resources to be shared.The object passedin here is a platformdependent native context object, and must not be deleted while this context may still be using it! To turn off sharing, you can call this method with a null pointer. Note: This must be called BEFORE attaching your context to a target component!