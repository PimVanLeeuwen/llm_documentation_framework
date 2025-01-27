#### copyToUTF16()


 size\_t String::copyToUTF16 ( CharPointer\_UTF16::CharType \* destBuffer, size\_t maxBufferSizeBytes ) const noexcept 
 

Copies the string to a buffer as UTF16 characters.Returns the number of bytes copied to the buffer, including the terminating null character.To find out how many bytes you need to store this string as UTF16, you can call CharPointer\_UTF16::getBytesRequiredFor (myString.getCharPointer())Parameters

 destBuffer the place to copy it to; if this is a null pointer, the method just returns the number of bytes required (including the terminating null character). 
 
 maxBufferSizeBytes the size of the destination buffer, in bytes. If the string won't fit, it'll put in as many as it can while still allowing for a terminating null char at the end, and will return the number of bytes that were actually used. 



See alsoCharPointer\_UTF16::writeWithDestByteLimit