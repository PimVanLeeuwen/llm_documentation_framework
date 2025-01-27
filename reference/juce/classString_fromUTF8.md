#### fromUTF8() [2/2]


 static String String::fromUTF8 ( const char8\_t \* utf8buffer, int bufferSizeBytes = 1 ) static 
 

Creates a String from a UTF8 encoded buffer.If the size is < 0, it'll keep reading until it hits a zero.