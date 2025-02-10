#### loadFileAsString()


 String File::loadFileAsString ( ) const 
 

Reads a file into memory as a string.Attempts to load the entire file as a zeroterminated string.This makes use of InputStream::readEntireStreamAsString, which can read either UTF16 or UTF8 file formats.