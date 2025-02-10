#### setPosition()


 bool MemoryInputStream::setPosition ( int64 newPosition ) overridevirtual 
 

Tries to move the current read position of the stream.The position is an absolute number of bytes from the stream's start.Some streams might not be able to do this, in which case they should do nothing and return false. Others might be able to manage it by resetting themselves and skipping to the correct position, although this is obviously a bit slow.Returnstrue if the stream manages to reposition itself correctly 
See alsogetPosition Implements InputStream.