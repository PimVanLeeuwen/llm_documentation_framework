#### incrementToEndOfWhitespace()


template<typename Type > 

 static void CharacterFunctions::incrementToEndOfWhitespace ( Type & text ) staticnoexcept 
 

Increments a pointer until it points to the first nonwhitespace character in a string.If the string contains only whitespace, the pointer will point to the string's null terminator.Referenced by CharPointer\_ASCII::incrementToEndOfWhitespace(), CharPointer\_UTF16::incrementToEndOfWhitespace(), CharPointer\_UTF32::incrementToEndOfWhitespace(), and CharPointer\_UTF8::incrementToEndOfWhitespace().