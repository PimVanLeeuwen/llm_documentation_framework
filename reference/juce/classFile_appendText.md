#### appendText()


 bool File::appendText ( const String & textToAppend, 
 
 bool asUnicode = false, 
 bool writeUnicodeHeaderBytes = false, 
 const char \* lineEndings = "\r\n" ) const 

Appends a string to the end of the file.This will try to append a text string to the file, as either 16bit unicode or 8bit characters in the default system encoding.It can also write the 'ff fe' unicode header bytes before the text to indicate the endianness of the file.If lineEndings is nullptr, then line endings in the text won't be modified. If you pass "\\n" or "\\r\\n" then this function will replace any existing line feeds.See alsoreplaceWithText