#### flush()


 void GZIPCompressorOutputStream::flush ( ) overridevirtual 
 

Flushes and closes the stream.Note that unlike most streams, when you call flush() on a GZIPCompressorOutputStream, the stream is closed this means that no more data can be written to it, and any subsequent attempts to call write() will cause an assertion.Implements OutputStream.