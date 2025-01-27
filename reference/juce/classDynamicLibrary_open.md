#### open()


 bool DynamicLibrary::open ( const String & name ) 
 

Opens a DLL.The name and the method by which it gets found is of course platformspecific, and may or may not include a path, depending on the OS. If a library is already open when this method is called, it will first close the library before attempting to load the new one.Returnstrue if the library was successfully found and opened.