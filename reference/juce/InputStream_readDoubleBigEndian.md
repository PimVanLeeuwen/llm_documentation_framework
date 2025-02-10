#### readDoubleBigEndian()


 virtual double InputStream::readDoubleBigEndian ( ) virtual 
 

Reads eight bytes as a 64bit floating point value.The raw 64bit encoding of the double is read from the stream as a bigendian int64. If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeDoubleBigEndian, readFloatBigEndian