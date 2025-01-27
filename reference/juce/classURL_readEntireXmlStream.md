#### readEntireXmlStream()


 std::unique\_ptr< XmlElement > URL::readEntireXmlStream ( bool usePostCommand = false ) const 
 

Tries to download the entire contents of this URL and parse it as XML.If it fails, or if the text that it reads can't be parsed as XML, this will return nullptr.Note that on some platforms (Android, for example) it's not permitted to do any network action from the message thread, so you must only call it from a background thread.Parameters

 usePostCommand whether to use a POST command to get the data (uses a GET command if this is false). 
 



See alsoreadEntireBinaryStream, readEntireTextStream