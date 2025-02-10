#### createInputStream()


 std::unique\_ptr< InputStream > URL::createInputStream ( const InputStreamOptions & options ) const 
 

Attempts to open a stream that can read from this URL.Note that this method will block until the first byte of data has been received or an error has occurred.Note that on some platforms (Android, for example) it's not permitted to do any network action from the message thread, so you must only call it from a background thread.Unless the URL represents a local file, this method returns an instance of a WebInputStream. You can use dynamic\_cast to cast the return value to a WebInputStream which allows you more finegrained control of the transfer process.If the URL represents a local file, then this method simply returns a FileInputStream.Parameters

 options a set of options that will be used when opening the stream. 
 



Returnsa valid input stream, or nullptr if there was an error trying to open it.