#### toCFString()


 CFStringRef String::toCFString ( ) const 
 

OSX ONLY Converts this string to a CFString.Remember that you must use CFRelease() to free the returned string when you're finished with it.