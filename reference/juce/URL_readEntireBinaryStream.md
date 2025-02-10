#### readEntireBinaryStream()


 bool URL::readEntireBinaryStream ( MemoryBlock & destData, 
 
 bool usePostCommand = false ) const 

Tries to download the entire contents of this URL into a binary data block.If it succeeds, this will return true and append the data it read onto the end of the memory block.Note that on some platforms (Android, for example) it's not permitted to do any network action from the message thread, so you must only call it from a background thread.Parameters

 destData the memory block to append the new data to. 
 
 usePostCommand whether to use a POST command to get the data (uses a GET command if this is false). 



See alsoreadEntireTextStream, readEntireXmlStream