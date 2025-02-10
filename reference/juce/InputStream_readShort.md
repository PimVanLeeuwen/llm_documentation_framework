#### readShort()


 virtual short InputStream::readShort ( ) virtual 
 

Reads two bytes from the stream as a littleendian 16bit value.If the next two bytes read are byte1 and byte2, this returns (byte1 (byte2 << 8)). If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeShort, readShortBigEndian