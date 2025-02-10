#### writeWithCharLimit()


template<typename CharPointer > 

 void CharPointer\_ASCII::writeWithCharLimit ( const CharPointer src, const int maxChars ) noexcept 
 

Copies a source string to this pointer, advancing this pointer as it goes.The maxChars parameter specifies the maximum number of characters that can be written to the destination buffer before stopping (including the terminating null).References CharacterFunctions::copyWithCharLimit().