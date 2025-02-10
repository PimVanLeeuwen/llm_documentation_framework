#### toWideCharPointer()


 const wchar\_t \* String::toWideCharPointer ( ) const 
 

Returns a pointer to a wchar\_t version of this string.Because it returns a reference to the string's internal data, the pointer that is returned must not be stored anywhere, as it can be deleted whenever the string changes.Bear in mind that the wchar\_t type is different on different platforms, so on Windows, this will be equivalent to calling toUTF16(), on unix it'll be the same as calling toUTF32(), etc.See alsogetCharPointer, toUTF8, toUTF16, toUTF32 Referenced by operator<<().