#### createFileWithoutCheckingPath()


 static File File::createFileWithoutCheckingPath ( const String & absolutePath ) staticnoexcept 
 

Creates a file that simply contains this string, without doing the sanitychecking that the normal constructors do.Best to avoid this unless you really know what you're doing.