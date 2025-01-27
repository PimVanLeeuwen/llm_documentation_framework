#### getTotalLength()


 int64 GZIPDecompressorInputStream::getTotalLength ( ) overridevirtual 
 

Returns the total number of bytes available for reading in this stream.Note that this is the number of bytes available from the start of the stream, not from the current position.If the size of the stream isn't actually known, this will return 1.See alsogetNumBytesRemaining Implements InputStream.