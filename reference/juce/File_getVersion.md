#### getVersion()


 String File::getVersion ( ) const 
 

If possible, this will try to create a version string for the given file.The OS may be able to look at the file and give a version for it e.g. with executables, bundles, dlls, etc. If no version is available, this will return an empty string.