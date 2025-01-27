#### preallocateBytes()


 void String::preallocateBytes ( size\_t numBytesNeeded ) 
 

Increases the string's internally allocated storage.Although the string's contents won't be affected by this call, it will increase the amount of memory allocated internally for the string to grow into.If you're about to make a large number of calls to methods such as += or <<, it's more efficient to preallocate enough extra space beforehand, so that these methods won't have to keep resizing the string to append the extra characters.Parameters

 numBytesNeeded the number of bytes to allocate storage for. If this value is less than the currently allocated size, it will have no effect. 
 


Referenced by Rectangle< ValueType >::toString().