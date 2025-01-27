#### writeWithDestByteLimit()


template<typename CharPointer > 

 size\_t CharPointer\_UTF32::writeWithDestByteLimit ( CharPointer src, size\_t maxDestBytes ) noexcept 
 

Copies a source string to this pointer, advancing this pointer as it goes.The maxDestBytes parameter specifies the maximum number of bytes that can be written to the destination buffer before stopping.References CharacterFunctions::copyWithDestByteLimit().