#### toUTF16()


 CharPointer\_UTF16 String::toUTF16 ( ) const 
 

Returns a pointer to a UTF16 version of this string.Because it returns a reference to the string's internal data, the pointer that is returned must not be stored anywhere, as it can be deleted whenever the string changes.To find out how many bytes you need to store this string as UTF16, you can call CharPointer\_UTF16::getBytesRequiredFor (myString.getCharPointer())See alsogetCharPointer, toUTF8, toUTF32