#### readDouble()


 virtual double InputStream::readDouble ( ) virtual 
 

Reads eight bytes as a 64bit floating point value.The raw 64bit encoding of the double is read from the stream as a littleendian int64. If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeDouble, readFloat