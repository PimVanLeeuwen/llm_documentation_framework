#### fromFile()


 static AndroidDocument AndroidDocument::fromFile ( const File & filePath ) static 
 

Create an AndroidDocument representing a file or directory at a particular path.This is provided for use on older API versions (lower than 19), or on other platforms, so that the same AndroidDocument API can be used regardless of the runtime platform version.If the runtime platform version is 19 or higher, and you wish to work with a URI obtained from a native file picker, use fromDocument() or fromTree() instead.If this function fails, hasValue() will return false on the returned document.