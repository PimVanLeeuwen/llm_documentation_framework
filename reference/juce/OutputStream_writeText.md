#### writeText()


 virtual bool OutputStream::writeText ( const String & text, bool asUTF16, bool writeUTF16ByteOrderMark, const char \* lineEndings ) virtual 
 

Writes a string of text to the stream.It can either write the text as UTF8 or UTF16, and can also add the UTF16 byteordermark bytes (0xff, 0xfe) to indicate the endianness (these should only be used at the start of a file).If lineEndings is nullptr, then line endings in the text won't be modified. If you pass "\\n" or "\\r\\n" then this function will replace any existing line feeds.Returnsfalse if the write operation fails for some reason