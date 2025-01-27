#### createStringFromData()


 static String String::createStringFromData ( const void \* data, int size ) static 
 

Creates a string from data in an unknown format.This looks at some binary data and tries to guess whether it's Unicode or 8bit characters, then returns a string that represents it correctly.Should be able to handle Unicode endianness correctly, by looking at the first two bytes.