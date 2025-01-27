#### encrypt() [3/3]


 int BlowFish::encrypt ( void \* buffer, size\_t sizeOfMsg, size\_t bufferSize ) const noexcept 
 

Encrypts data inplace.Parameters

 buffer The message that should be encrypted. See bufferSize on size requirements! 
 
 sizeOfMsg The size of the message that should be encrypted in bytes 
 bufferSize The size of the buffer in bytes. To accommodate the encrypted data, the buffer must be larger than the message: the size of the buffer needs to be equal or greater than the size of the message in bytes rounded to the next integer which is divisible by eight. If the message size in bytes is already divisible by eight then you need to add eight bytes to the buffer size. If in doubt simply use bufferSize = sizeOfMsg + 8. 



ReturnsThe size of the decrypted data in bytes or 1 if the decryption failed.