#### readEntireStreamAsString()


 virtual String InputStream::readEntireStreamAsString ( ) virtual 
 

Tries to read the whole stream and turn it into a string.This will read from the stream's current position until the endofstream. It can read from UTF8 data, or UTF16 if it detects suitable headerbytes.