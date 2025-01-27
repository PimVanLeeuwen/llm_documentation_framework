#### addEntry()


 void ZipFile::Builder::addEntry ( InputStream \* streamToRead, 
 
 int compressionLevel, 
 const String & storedPathName, 
 Time fileModificationTime ) 

Adds a stream to the list of items which will be added to the archive.Parameters

 streamToRead this stream isn't read immediately a pointer to the stream is stored, then used later when the writeToStream() method is called, and deleted by the Builder object when no longer needed, so be very careful about its lifetime and the lifetime of any objects on which it depends! This must not be null. 
 
 compressionLevel this can be between 0 (no compression), and 9 (maximum compression). 
 storedPathName the partial pathname that will be stored for this file 
 fileModificationTime the timestamp that will be stored as the last modification time of this entry