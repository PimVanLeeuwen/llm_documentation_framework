#### readShortBigEndian()


 virtual short InputStream::readShortBigEndian ( ) virtual 
 

Reads two bytes from the stream as a littleendian 16bit value.If the next two bytes read are byte1 and byte2, this returns (byte2 (byte1 << 8)). If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeShortBigEndian, readShort