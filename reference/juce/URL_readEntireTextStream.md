#### readEntireTextStream()


 String URL::readEntireTextStream ( bool usePostCommand = false ) const 
 

Tries to download the entire contents of this URL as a string.If it fails, this will return an empty string, otherwise it will return the contents of the downloaded file. If you need to distinguish between a read operation that fails and one that returns an empty string, you'll need to use a different method, such as readEntireBinaryStream().Note that on some platforms (Android, for example) it's not permitted to do any network action from the message thread, so you must only call it from a background thread.Parameters

 usePostCommand whether to use a POST command to get the data (uses a GET command if this is false). 
 



See alsoreadEntireBinaryStream, readEntireXmlStream