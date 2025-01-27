#### writeWithCharLimit()


template<typename CharPointer > 

 void CharPointer\_UTF32::writeWithCharLimit ( CharPointer src, int maxChars ) noexcept 
 

Copies a source string to this pointer, advancing this pointer as it goes.The maxChars parameter specifies the maximum number of characters that can be written to the destination buffer before stopping (including the terminating null).References CharacterFunctions::copyWithCharLimit().