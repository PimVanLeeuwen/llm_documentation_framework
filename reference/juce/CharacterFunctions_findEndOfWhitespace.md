#### findEndOfWhitespace()


template<typename Type > 

 static Type CharacterFunctions::findEndOfWhitespace ( Type text ) staticnoexcept 
 

Returns a pointer to the first nonwhitespace character in a string.If the string contains only whitespace, this will return a pointer to its null terminator.Referenced by CharPointer\_ASCII::findEndOfWhitespace(), CharPointer\_UTF16::findEndOfWhitespace(), CharPointer\_UTF32::findEndOfWhitespace(), and CharPointer\_UTF8::findEndOfWhitespace().