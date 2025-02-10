#### getCharPointer()


 CharPointerType String::getCharPointer ( ) const noexcept 
 

Returns the character pointer currently being used to store this string.Because it returns a reference to the string's internal data, the pointer that is returned must not be stored anywhere, as it can be deleted whenever the string changes.