#### readIntBigEndian()


 virtual int InputStream::readIntBigEndian ( ) virtual 
 

Reads four bytes from the stream as a bigendian 32bit value.If the next four bytes are byte1 to byte4, this returns (byte4 (byte3 << 8) (byte2 << 16) (byte1 << 24)).If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeIntBigEndian, readInt