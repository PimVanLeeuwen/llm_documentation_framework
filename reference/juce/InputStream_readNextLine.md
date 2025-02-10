#### readNextLine()


 virtual String InputStream::readNextLine ( ) virtual 
 

Reads a UTF8 string from the stream, up to the next linefeed or carriage return.This will read up to the next "\n" or "\r\n" or endofstream.After this call, the stream's position will be left pointing to the next character following the linefeed, but the linefeeds aren't included in the string that is returned.