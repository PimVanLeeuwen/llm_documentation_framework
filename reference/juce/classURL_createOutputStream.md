#### createOutputStream()


 std::unique\_ptr< OutputStream > URL::createOutputStream ( ) const 
 

Attempts to open an output stream to a URL for writing.This method can only be used for certain scheme types such as local files and content:// URIs on Android.