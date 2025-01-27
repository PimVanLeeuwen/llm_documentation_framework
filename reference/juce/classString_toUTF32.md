#### toUTF32()


 CharPointer\_UTF32 String::toUTF32 ( ) const 
 

Returns a pointer to a UTF32 version of this string.Because it returns a reference to the string's internal data, the pointer that is returned must not be stored anywhere, as it can be deleted whenever the string changes.See alsogetCharPointer, toUTF8, toUTF16