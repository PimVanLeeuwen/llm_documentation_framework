#### readInt64BigEndian()


 virtual int64 InputStream::readInt64BigEndian ( ) virtual 
 

Reads eight bytes from the stream as a bigendian 64bit value.If the next eight bytes are byte1 to byte8, this returns (byte8 (byte7 << 8) (byte6 << 16) (byte5 << 24) (byte4 << 32) (byte3 << 40) (byte2 << 48) (byte1 << 56)).If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeInt64BigEndian, readInt64