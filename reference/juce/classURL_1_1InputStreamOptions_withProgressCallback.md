#### withProgressCallback()


 InputStreamOptions URL::InputStreamOptions::withProgressCallback ( std::function< bool(int bytesSent, int totalBytes)> progressCallback ) const nodiscard 
 

A callback function to keep track of the operation's progress.This can be useful for lengthy POST operations, so that you can provide user feedback.