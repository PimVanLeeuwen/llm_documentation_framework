#### getNativeHandle()


 void \* DynamicLibrary::getNativeHandle ( ) const noexcept 
 

Returns the platformspecific native library handle.You'll need to cast this to whatever is appropriate for the OS that's in use.