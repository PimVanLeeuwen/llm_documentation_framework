#### getRawContext()


 void \* OpenGLContext::getRawContext ( ) const noexcept 
 

Returns an OSdependent handle to some kind of underlying OSprovided GL context.The exact type of the value returned will depend on the OS and may change if the implementation changes. If you want to use this, digging around in the native code is probably the best way to find out what it is.