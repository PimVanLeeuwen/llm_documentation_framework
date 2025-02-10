#### getTotalLength()


 int64 WebInputStream::getTotalLength ( ) overridevirtual 
 

Returns the total number of bytes available for reading in this stream.Note that this is the number of bytes available from the start of the stream, not from the current position.If getTotalLength() is called without an established connection, then getTotalLength() will call connect internally and block until connect returns either due to a successful connection or a connection error.If the size of the stream isn't actually known, this will return 1.Implements InputStream.