#### readInt()


 virtual int InputStream::readInt ( ) virtual 
 

Reads four bytes from the stream as a littleendian 32bit value.If the next four bytes are byte1 to byte4, this returns (byte1 (byte2 << 8) (byte3 << 16) (byte4 << 24)).If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeInt, readIntBigEndian