#### setPosition()


 virtual bool OutputStream::setPosition ( int64 newPosition ) pure virtual 
 

Tries to move the stream's output position.Not all streams will be able to seek to a new position this will return false if it fails to work.See alsogetPosition Implemented in ARAOutputStream, FileOutputStream, GZIPCompressorOutputStream, and MemoryOutputStream.