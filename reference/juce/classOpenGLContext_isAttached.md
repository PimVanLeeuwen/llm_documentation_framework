#### isAttached()


 bool OpenGLContext::isAttached ( ) const noexcept 
 

Returns true if the context is attached to a component and is onscreen.Note that if you call attachTo() for a nonvisible component, this method will return false until the component is made visible.