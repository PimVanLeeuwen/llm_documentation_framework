#### hasFileExtension()


 bool File::hasFileExtension ( StringRef extensionToTest ) const 
 

Checks whether the file has a given extension.Parameters

 extensionToTest the extension to look for it doesn't matter whether or not this string has a dot at the start, so ".wav" and "wav" will have the same effect. To compare with multiple extensions, this parameter can contain multiple strings, separated by semicolons so, for example: hasFileExtension (".jpeg;png;gif") would return true if the file has any of those three extensions. 
 



See alsogetFileExtension, withFileExtension, getFileNameWithoutExtension