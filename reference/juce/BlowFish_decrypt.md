#### decrypt() [3/3]


 int BlowFish::decrypt ( void \* buffer, size\_t bytes ) const noexcept 
 

Decrypts data inplace.Parameters

 buffer The encrypted data that should be decrypted 
 
 bytes The size of the encrypted data in bytes 



ReturnsThe size of the decrypted data in bytes or 1 if the decryption failed.