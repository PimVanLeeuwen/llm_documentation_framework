#### writeString()


 virtual bool OutputStream::writeString ( const String & text ) virtual 
 

Stores a string in the stream in a binary format.This isn't the method to use if you're trying to append text to the end of a textfile! It's intended for storing a string so that it can be retrieved later by InputStream::readString().It writes the string to the stream as UTF8, including the null termination character.For appending text to a file, instead use writeText, or operator<<Returnsfalse if the write operation fails for some reason 
See alsoInputStream::readString, writeText, operator<<