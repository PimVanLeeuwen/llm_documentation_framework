#### readInt64()


 virtual int64 InputStream::readInt64 ( ) virtual 
 

Reads eight bytes from the stream as a littleendian 64bit value.If the next eight bytes are byte1 to byte8, this returns (byte1 (byte2 << 8) (byte3 << 16) (byte4 << 24) (byte5 << 32) (byte6 << 40) (byte7 << 48) (byte8 << 56)).If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeInt64, readInt64BigEndian