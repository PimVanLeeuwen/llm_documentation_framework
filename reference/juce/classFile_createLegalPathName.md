#### createLegalPathName()


 static String File::createLegalPathName ( const String & pathNameToFix ) static 
 

Returns a version of a path with any illegal characters removed.Similar to createLegalFileName(), but this won't remove slashes, so can be used on a complete pathname.See alsocreateLegalFileName