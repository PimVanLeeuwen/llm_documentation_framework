#### copyWithDestByteLimit()


template<typename DestCharPointerType , typename SrcCharPointerType > 

 static size\_t CharacterFunctions::copyWithDestByteLimit ( DestCharPointerType & dest, SrcCharPointerType src, size\_t maxBytesToWrite ) staticnoexcept 
 

Copies characters from one string to another, up to a null terminator or a given byte size limit.References getAddressDifference().Referenced by CharPointer\_ASCII::writeWithDestByteLimit(), CharPointer\_UTF16::writeWithDestByteLimit(), CharPointer\_UTF32::writeWithDestByteLimit(), and CharPointer\_UTF8::writeWithDestByteLimit().