#### copyWithCharLimit()


template<typename DestCharPointerType , typename SrcCharPointerType > 

 static void CharacterFunctions::copyWithCharLimit ( DestCharPointerType & dest, SrcCharPointerType src, int maxChars ) staticnoexcept 
 

Copies characters from one string to another, up to a null terminator or a given maximum number of characters.Referenced by CharPointer\_ASCII::writeWithCharLimit(), CharPointer\_UTF16::writeWithCharLimit(), CharPointer\_UTF32::writeWithCharLimit(), and CharPointer\_UTF8::writeWithCharLimit().