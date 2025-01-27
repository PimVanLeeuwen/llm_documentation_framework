#### setPosition()


 bool ARAOutputStream::setPosition ( int64 newPosition ) overridevirtual 
 

Tries to move the stream's output position.Not all streams will be able to seek to a new position this will return false if it fails to work.See alsogetPosition Implements OutputStream.