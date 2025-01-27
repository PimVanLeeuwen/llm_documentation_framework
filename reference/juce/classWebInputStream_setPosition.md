#### setPosition()


 bool WebInputStream::setPosition ( int64 wantedPos ) overridevirtual 
 

Tries to move the current read position of the stream.The position is an absolute number of bytes from the stream's start.For a WebInputStream, this method will fail if wantedPos is smaller than the current position. If wantedPos is greater than the current position, then calling setPosition() is the same as calling read(), i.e. the skipped data will still be downloaded, although skipped bytes will be discarded immediately.Returnstrue if the stream manages to reposition itself correctly 
See alsogetPosition Implements InputStream.