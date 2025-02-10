#### find() [2/2]


template<typename CharPointerType > 

 static CharPointerType CharacterFunctions::find ( CharPointerType textToSearch, const juce\_wchar charToLookFor ) staticnoexcept 
 

Returns a pointer to the first occurrence of a substring in a string.If the substring is not found, this will return a pointer to the string's null terminator.