#### getFunction()


 void \* DynamicLibrary::getFunction ( const String & functionName ) noexcept 
 

Tries to find a named function in the currentlyopen DLL, and returns a pointer to it.If no library is open, or if the function isn't found, this will return a null pointer.