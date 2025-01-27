#### readBool()


 virtual bool InputStream::readBool ( ) virtual 
 

Reads a boolean from the stream.The bool is encoded as a single byte nonzero for true, 0 for false. If the stream is exhausted, this will return false.See alsoOutputStream::writeBool