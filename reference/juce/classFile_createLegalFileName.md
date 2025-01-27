#### createLegalFileName()


 static String File::createLegalFileName ( const String & fileNameToFix ) static 
 

Returns a version of a filename with any illegal characters removed.This will return a copy of the given string after removing characters that are not allowed in a legal filename, and possibly shortening the string if it's too long.Because this will remove slashes, don't use it on an absolute pathname use createLegalPathName() for that.See alsocreateLegalPathName