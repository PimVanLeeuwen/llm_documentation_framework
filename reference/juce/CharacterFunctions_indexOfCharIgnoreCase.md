#### indexOfCharIgnoreCase()


template<typename Type > 

 static int CharacterFunctions::indexOfCharIgnoreCase ( Type text, juce\_wchar charToFind ) staticnoexcept 
 

Finds the character index of a given character in another string, using a caseindependent match.Returns 1 if the character is not found.References toLowerCase().Referenced by CharPointer\_ASCII::indexOf(), CharPointer\_UTF16::indexOf(), CharPointer\_UTF32::indexOf(), and CharPointer\_UTF8::indexOf().