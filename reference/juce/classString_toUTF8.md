#### toUTF8()


 CharPointer\_UTF8 String::toUTF8 ( ) const 
 

Returns a pointer to a UTF8 version of this string.Because it returns a reference to the string's internal data, the pointer that is returned must not be stored anywhere, as it can be deleted whenever the string changes.To find out how many bytes you need to store this string as UTF8, you can call CharPointer\_UTF8::getBytesRequiredFor (myString.getCharPointer())See alsotoRawUTF8, getCharPointer, toUTF16, toUTF32