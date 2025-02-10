#### readFloat()


 virtual float InputStream::readFloat ( ) virtual 
 

Reads four bytes as a 32bit floating point value.The raw 32bit encoding of the float is read from the stream as a littleendian int. If the stream is exhausted partway through reading the bytes, this will return zero.See alsoOutputStream::writeFloat, readDouble